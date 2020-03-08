from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    process = models.CharField(max_length=200)
    image = models.ImageField()
    date = models.DateField("prepared_date")

    def __str__ (self):
        return self.name




