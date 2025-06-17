from django.db import models

class CartModel(models.Model):
    item_name = models.CharField(max_length=100)
    item_quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)