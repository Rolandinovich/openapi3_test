from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True,)
    email = models.EmailField(max_length=40, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

