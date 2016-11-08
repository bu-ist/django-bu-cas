from django.contrib import admin
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm

class WebloginUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Weblogin username"
        self.fields['username'].required = True
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    def clean_password2(self):
        return self.cleaned_data.get("password2")


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    add_form = WebloginUserCreationForm
    list_display = ('username', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',)}
        ),
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

    # Weblogin automatically creates users as non-staff users.
    # If added in the admin, they are assumed to be staff.
    def save_model(self, request, user, form_form, change):
        user.is_staff = True
        if( not user.email or user.email == "" ):
        	user.email = user.username + "@bu.edu"
        super(UserAdmin,self).save_model(request, user, form_form, change)


# first unregister the existing useradmin...
admin.site.unregister(User)

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)