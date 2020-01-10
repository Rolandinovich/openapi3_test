from django.db import models
from django.utils.translation import ugettext as _

from recipe.models import Recipe


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name=_('Recipe'), on_delete=models.CASCADE)
    data = models.DateTimeField(_('Created'), auto_now_add=True)
    text = models.TextField(_('Text'))
