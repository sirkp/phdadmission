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
        exclude = ('user','application_no','first_name','last_name','email')

    # def get_initial(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['user']=self.request.user
    #     self.fields['first_name']=self.request.user.first_name
    #     self.fields['last_name']=self.request.user.first_name
    #     self.fields['email']=self.request.user.email
