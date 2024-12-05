from django.db import models
from pkg_resources import require


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=8)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    size = models.DecimalField(decimal_places=3, max_digits=7)
    description = models.TextField()
    age_limited = models.BooleanField(False)
    buyers = models.ManyToManyField(Buyer, related_name="games")




