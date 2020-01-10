from django.db import models
from django.utils.translation import ugettext as _

from recipe.models import Recipe
from user.models import User


class Feedback(models.Model):
    date = models.DateTimeField(_('Date created'), auto_now_add=True)
    recipe = models.ForeignKey(Recipe, verbose_name=_('Recipe'), on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    dosage = models.FloatField('Dosage')
    answers = models.TextField(_('Answers after usage'))
