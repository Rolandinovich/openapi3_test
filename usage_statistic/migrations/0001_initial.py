# Generated by Django 2.2.7 on 2020-01-10 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('dosage', models.FloatField(verbose_name='Dosage')),
                ('answers', models.TextField(verbose_name='Answers after usage')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipe.Recipe', verbose_name='Recipe')),
            ],
        ),
    ]
