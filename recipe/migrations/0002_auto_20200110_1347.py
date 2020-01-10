# Generated by Django 2.2.7 on 2020-01-10 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='source_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipe.RecipeImage'),
        ),
        migrations.AddField(
            model_name='ingredientsentity',
            name='cartridge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipe.Cartridge', verbose_name='Cartridge'),
        ),
        migrations.AddField(
            model_name='ingredientsentity',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Substance', verbose_name='Substance'),
        ),
        migrations.AddField(
            model_name='individualdosage',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe', verbose_name='Recipe'),
        ),
        migrations.AddField(
            model_name='individualdosage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='cartridgeinrecipe',
            name='cartridge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Cartridge', verbose_name='Cartridge'),
        ),
        migrations.AddField(
            model_name='cartridgeinrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartridges_in_recipe', to='recipe.Recipe', verbose_name='Recipe'),
        ),
    ]
