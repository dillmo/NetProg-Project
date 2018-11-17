from django.db import models

class User(models.Model):
    username     = models.CharField(max_length=50)
    email        = models.EmailField()
    # Passwords are stored in plaintext because we're pressed for time
    password     = models.CharField(max_length=50)

class Product(models.Model):
    image = models.ImageField()
    name  = models.CharField(max_length=100)
    price = models.IntegerField()            # Stored as a number of cents
    stock = models.IntegerField()