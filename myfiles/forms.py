from django import forms
from myfiles.models import Announcement, OMRSheet

class AnnouncementsForm(forms.ModelForm):
    """
    form to upload a single announcements(file or image) at a time
    """
    class Meta:
        model = Announcement
        fields = ('title', 'my_file')

class OMRSheetsForm(forms.ModelForm):
    """
    form to upload multiple omrsheet images 
    """
    class Meta:
        model = OMRSheet
        fields = ('my_images',)
