from django.contrib import admin
from django.contrib.admin import AdminSite
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin

from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from django_bucas import sites

class MyAdminSite(AdminSite):

    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()

        #replace the logout url with the cas backend url.
        for i in range(len(urls)):
            patt = urls[i]
            if not hasattr(patt, 'name'):
                continue
            if patt.name == 'logout':
                urls.remove(patt)
                break;

        urls += sites.urls[0]
        return urls

site = MyAdminSite()
admin.site = site
admin.site.register(Group, GroupAdmin)

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
        if( not user.email or user.email == "" ):
            user.email = user.username + "@bu.edu"
        super(CASUserAdmin,self).save_model(request, user, form_form, change)


# Now register the new UserAdmin...
# admin.site.unregister(User)
admin.site.register(User, CASUserAdmin)
