from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from accounts.models import User
from django.utils.translation import ugettext_lazy as _
import unicodedata

UserModel = get_user_model()

class LoginForm(AuthenticationForm):
    """
    This form is linked with model User, it determines the fields in log in page
    """
    model = User
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"

    def clean(self):
        """
        It checks if user is locked
        """
        my_cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        myuser = get_object_or_404(User, username=username)
        if(myuser.is_locked):
            raise forms.ValidationError(_("You are locked"))
        return my_cleaned_data

class SignupForm(UserCreationForm):
    """
    it determines the fields in  sign up page
    """

    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'password1', 'password2')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for fieldname in [ 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_email(self):
        """
        Checks if email is already in use
        """
        email = self.cleaned_data.get('email')

        if email in User.objects.all().values_list('email', flat=True) or email in User.objects.all().values_list('email', flat=True):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return email
