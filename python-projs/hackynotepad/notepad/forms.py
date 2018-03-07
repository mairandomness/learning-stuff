from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django import forms


class UserAdminAuthenticationForm(AuthenticationForm):
    """
    Custom authentication
    """
    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': _(
            "Please enter the correct %(username)s and password for a staff "
            "account. Note that both fields may be case-sensitive."
        ),
    }


    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)


