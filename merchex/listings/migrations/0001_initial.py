# Generated by Django 5.0.7 on 2024-07-23 15:17

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('BG', 'Bagarre'), ('CS', 'Croissant')], default='HH', max_length=5)),
                ('biography', models.CharField(blank=True, max_length=1000, null=True)),
                ('year_formed', models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1900, 'La valeur minimale est 1900'), django.core.validators.MaxValueValidator(2024, 'La valeur maximale est 2024')])),
                ('active', models.BooleanField(default=True)),
                ('official_homepage', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('article', models.CharField(max_length=1000)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
