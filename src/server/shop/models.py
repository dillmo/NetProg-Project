from django.db import models

class Product(models.Model):
    image = models.ImageField()
    name  = models.CharField(max_length=100)
    price = models.IntegerField()            # Stored as a number of cents
    stock = models.IntegerField()