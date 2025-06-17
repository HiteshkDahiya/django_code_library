from django.db import models

#Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)