from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

class Band(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        BAGARRE = 'BG'
        CROISSANT = 'CS'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, default= 'HH')
    biography = models.fields.CharField(max_length=1000, null=True, blank=True)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900, 'La valeur minimale est 1900'), MaxValueValidator(2024, 'La valeur maximale est 2024')], default=2000)
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class New(models.Model):

    def __str__(self):
        return f'{self.title}'

    title = models.fields.CharField(max_length=100)
    article = models.fields.CharField(max_length=1000)
    date = models.fields.DateField(default=date.today)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
