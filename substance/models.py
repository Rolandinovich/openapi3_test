from django.db import models


# Create your models here.


class Substance(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
