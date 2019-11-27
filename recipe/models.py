from django.db import models

# Create your models here.
from cartridge.models import Cartridge


class Recipe(models.Model):
    name = models.CharField(max_length=50)


class CartridgeInRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    cartridge = models.ForeignKey(Cartridge, on_delete=models.CASCADE)
    amount = models.FloatField()
