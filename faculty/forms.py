from django import forms
from phdfellows.models import Application
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class StudentApplicationForm(forms.ModelForm):
    """
    Form to change the application current status
    """
    class Meta():
        model = Application
        fields = ('current_status',)
