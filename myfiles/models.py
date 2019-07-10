from django.db import models

# Create your models here.
class Announcements(models.Model):
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
