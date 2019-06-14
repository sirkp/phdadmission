from django import forms
from faculty.models import Email,Faculty
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    model = Faculty
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = Faculty
        fields = ('first_name','last_name', 'email', 'password1', 'password2')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for fieldname in [ 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email not in Email.objects.all().values_list('email', flat=True):
            raise forms.ValidationError(_("This email is not in registered faculty email list, Please try with official IIT Ropar email"))
        return email
