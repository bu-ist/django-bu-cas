from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin,  GroupAdmin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import RedirectView

class WebloginUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Weblogin username"
        self.fields['username'].required = True
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    def clean_password2(self):
        return self.cleaned_data.get("password2")


class CASUserAdmin(UserAdmin):
    # The forms to add and change user instances
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    add_form = WebloginUserCreationForm
    list_display = ('username', 'is_staff', 'is_superuser')

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',)}
        ),
    )

    # Weblogin automatically creates users as non-staff users.
    # If added in the admin, they are assumed to be staff.
    def save_model(self, request, user, form_form, change):
        user.is_active = True
        user.set_password(None)
        if( not user.email or user.email == "" ):
            user.email = user.username + "@bu.edu"
        super(CASUserAdmin,self).save_model(request, user, form_form, change)


# Now register the new UserAdmin...
admin.site.unregister(User)
admin.site.register(User, CASUserAdmin)