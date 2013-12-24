from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from prv.models import *
from registration.forms import RegistrationFormTermsOfService


class SupplierInfoForm(forms.ModelForm):

    class Meta:
        model = SupplierInfo


class CustomRegistrationForm(RegistrationFormTermsOfService):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Username', 'class': 'form-control', 'required': 'true'
    }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Email', 'class': 'form-control', 'required': 'true'
    }))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={
        'placeholder': 'Password', 'class': 'form-control', 'required': 'true'
    }))
    password2 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={
        'placeholder': 'Password', 'class': 'form-control', 'required': 'true'
    }))
    terms = forms.CharField(required=True, widget=forms.Textarea(attrs={
       'class': 'form-control', 'readonly': True, 'required': 'false'
    }))

    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['terms'].required = False

class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Username', 'class': 'form-control', 'id': 'uname', 'required': 'true'
    }))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={
        'placeholder': 'Password', 'class': 'form-control', 'id': 'password', 'required': 'true'
    }))

    error_messages = {
        'invalid_login': _("Invalid username or password. Please try again. "
                           "Note that both fields may be case-sensitive."),
        'no_cookies': _("Your Web browser doesn't appear to have cookies "
                        "enabled. Cookies are required for logging in."),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            username = User.objects.get(username=username)
        except:
            raise forms.ValidationError('Invalid username or password. Please try again.')

        if username and password:
            self.user_cache = authenticate(username=username.username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login']
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(self.error_messages['no_cookies'])

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
