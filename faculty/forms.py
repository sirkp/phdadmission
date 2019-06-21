from django import forms
from faculty.models import Email
from phdfellows.models import Application
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class StudentApplicationForm(forms.ModelForm):
    class Meta():
        model = Application
        fields = ('current_status',)
