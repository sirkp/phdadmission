from django import forms
from myfiles.models import Announcement, OMRSheet

class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'my_file')

class OMRSheetsForm(forms.ModelForm):
    class Meta:
        model = OMRSheet
        fields = ('my_images',)
