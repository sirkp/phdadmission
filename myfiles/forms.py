from django import forms
from myfiles.models import Announcements

class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ('title', 'my_file')
