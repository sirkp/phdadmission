from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class PhdFellows(User,PermissionsMixin):
    def __str__(self):
        return self.first_name+" "+self.last_name
