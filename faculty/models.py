from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
# Create your models here.
class Email(models.Model):
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.email

class Faculty(User,PermissionsMixin):
    def __str__(self):
        return self.first_name+" "+self.last_name
