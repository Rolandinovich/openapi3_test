from django.db import models
# Create your models here.
from django.utils.translation import ugettext as _

from recipe.utils.roleenum import BaseEnum
from user.models import User


class RecipeImage(models.Model):
    name = models.CharField(_('Image name'), max_length=50, null=True, blank=True)
    image = models.ImageField(
        upload_to='images',
        verbose_name=_('Image'),
        blank=True, null=True)


class Recipe(models.Model):
    description_text = models.TextField(_('Description Text'),
                                        null=True, blank=True)
    internal_name = models.CharField(_('Internal name'), max_length=50)
    name = models.CharField(_('Name'), max_length=255)
    rate = models.PositiveIntegerField(_('Rate'),
                                       blank=True, null=True)
    source_image = models.ForeignKey(RecipeImage, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, verbose_name=_('Owner'), on_delete=models.PROTECT)


class Cartridge(models.Model):
    color = models.CharField(_('Color'), max_length=10)
    max_volume = models.FloatField(_('Max volume, ml'))
    name = models.CharField(_('Name'), max_length=100)


class CartridgeInRecipe(models.Model):
    order_number = models.PositiveIntegerField(_('Order number'))
    percent = models.FloatField(_('Percent'))
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name=_('Recipe'),
                               related_name='cartridges_in_recipe')
    cartridge = models.ForeignKey(Cartridge,
                                  on_delete=models.CASCADE,
                                  verbose_name=_('Cartridge'))


class SubstanceTypeChoice(BaseEnum):
    TERPEN = _('terpen')
    CANABIN = _('canabinoid')


class Substance(models.Model):
    type = models.CharField(verbose_name='Type', max_length=30,
                            choices=SubstanceTypeChoice.get_choices(), blank=True, null=True)
    name = models.CharField(_('Name'), max_length=50)
    abbreviation = models.CharField(_('Abbreviation'), max_length=255)
    color = models.CharField(_('Color'), max_length=10)
    description_text = models.TextField(_('Description Text'),
                                        null=True, blank=True)


class Ingredient(models.Model):
    amount = models.FloatField(_('Amount, ml'), default=0)
    type = models.ForeignKey(Substance,
                             on_delete=models.CASCADE,
                             verbose_name=_('Substance'))
    cartridge = models.ForeignKey(Cartridge,
                                  on_delete=models.CASCADE,
                                  verbose_name=_('Cartridge'),
                                  related_name='ingredients')


class IndividualDosage(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, verbose_name=_('Recipe'), on_delete=models.CASCADE)
    low = models.FloatField(_('low dosage'))
    medium = models.FloatField(_('medium dosage'))
    heroic = models.FloatField(_('heroic dosage'))
