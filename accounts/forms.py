from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth import get_user_model, authenticate
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from accounts.models import User
from django.utils.translation import ugettext_lazy as _
import unicodedata

UserModel = get_user_model()

class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs['autocapitalize'] = 'none'
        return attrs

class LoginForm(AuthenticationForm):
    model = User
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"

    def clean(self):

        my_cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        myuser = get_object_or_404(User, username=username)
        if(myuser.is_locked):
            raise forms.ValidationError(_("You are locked"))
        return my_cleaned_data

# class LoginForm(forms.Form):
#     """
#     Base class for authenticating users. Extend this to get a form that accepts
#     username/password logins.
#     """
#     username = UsernameField(widget=forms.TextInput(attrs={'autocomplete': 'username', 'autofocus': True}))
#     password = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
#     )
#
#     error_messages = {
#         'invalid_login': _(
#             "Please enter a correct %(username)s and password. Note that both "
#             "fields may be case-sensitive."
#         ),
#         'inactive': _("This account is inactive."),
#     }
#
#     def __init__(self, request=None, *args, **kwargs):
#         """
#         The 'request' parameter is set for custom auth use by subclasses.
#         The form data comes in via the standard 'data' kwarg.
#         """
#         self.request = request
#         self.user_cache = None
#         super().__init__(*args, **kwargs)
#
#         # Set the max length and label for the "username" field.
#         self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
#         self.fields['username'].max_length = self.username_field.max_length or 254
#         self.fields['username'].label = "Email"
#         if self.fields['username'].label is None:
#             self.fields['username'].label = capfirst(self.username_field.verbose_name)
#
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#         if username is not None and password:
#             self.user_cache = authenticate(self.request, username=username, password=password)
#             if self.user_cache is None:
#                 raise self.get_invalid_login_error()
#             else:
#                 self.confirm_login_allowed(self.user_cache)
#
#         myuser = get_object_or_404(User, username=username)
#         if(myuser.is_locked):
#             raise forms.ValidationError(_("You are locked"))
#
#         return self.cleaned_data
#
#     def confirm_login_allowed(self, user):
#         """
#         Controls whether the given User may log in. This is a policy setting,
#         independent of end-user authentication. This default behavior is to
#         allow login by active users, and reject login by inactive users.
#         If the given user cannot log in, this method should raise a
#         ``forms.ValidationError``.
#         If the given user may log in, this method should return None.
#         """
#         if not user.is_active:
#             raise forms.ValidationError(
#                 self.error_messages['inactive'],
#                 code='inactive',
#             )
#
#     def get_user(self):
#         return self.user_cache
#
#     def get_invalid_login_error(self):
#         return forms.ValidationError(
#             self.error_messages['invalid_login'],
#             code='invalid_login',
#             params={'username': self.username_field.verbose_name},
#         )


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'password1', 'password2')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for fieldname in [ 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email in User.objects.all().values_list('email', flat=True) or email in User.objects.all().values_list('email', flat=True):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return email
