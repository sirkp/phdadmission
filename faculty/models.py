from django.db import models
from accounts.models import User
from phdfellows.models import Application
# Create your models here.
class ApplicantScoreByFaculty(models.Model):
    """
    Model for assessment of applicants after selection by faculty 
    """
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)
    application_no = models.OneToOneField(Application, on_delete=models.CASCADE)
    willing_to_guide_choices = [
        ('Yes','Yes'),
        ('No','No'),
    ]
    willing_to_guide = models.CharField(choices=willing_to_guide_choices,max_length=3)
    assesment_score = models.IntegerField(null=True)
    remarks = models.TextField()
