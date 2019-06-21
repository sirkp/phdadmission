from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.models import User
from accounts.models import User
from django.utils.translation import ugettext_lazy as _

class LoginForm(AuthenticationForm):
    model = User
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"

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
