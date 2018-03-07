from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .forms import UserAdminAuthenticationForm
from django.contrib.auth.models import Permission

from .models import Note


class UserAdmin(AdminSite):

    login_form = UserAdminAuthenticationForm

    def has_permission(self, request):
        return request.user.is_active


user_admin_site = UserAdmin(name='useradmin')

user_admin_site.register(Note)


admin.site.register(Note)
