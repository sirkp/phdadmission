from django.db import models

# Create your models here.
class Announcement(models.Model):
    """
    model for announcements(notice)
    """
    title = models.CharField(max_length=500)
    my_file = models.FileField(upload_to='announcements/')
    date_uploaded = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.my_file.delete()
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['-date_uploaded']

class OMRSheet(models.Model):
    """
    model for omr sheet images
    """
    my_images = models.ImageField(upload_to='omr_sheets/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-uploaded_at']

    def delete(self, *args, **kwargs):
        self.my_images.delete()
        super().delete(*args, **kwargs)
