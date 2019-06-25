from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name+" "+self.last_name
