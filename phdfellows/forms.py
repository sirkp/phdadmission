from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phdfellows.models import PhdFellows,Application
from django.utils.translation import ugettext_lazy as _

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = PhdFellows
        fields = ('first_name','last_name', 'email', 'password1', 'password2')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for fieldname in [ 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email in PhdFellows.objects.all().values_list('email', flat=True) or email in User.objects.all().values_list('email', flat=True):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return email

class ApplicationForm(forms.ModelForm):
    class Meta():
        model = Application
        exclude = ('submitted_at','current_status','previous_status','user','application_no','first_name','last_name','email')

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
