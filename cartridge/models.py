from django.db import models

# Create your models here.
from substance.models import Substance


class Cartridge(models.Model):
    name = models.CharField(max_length=50)
    volume = models.PositiveIntegerField()
    substances = models.ForeignKey(Substance, on_delete=models.CASCADE)

