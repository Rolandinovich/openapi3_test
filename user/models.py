from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    photo = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=40, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
