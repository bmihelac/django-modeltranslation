from django.db import models


class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=250)
    

class ProductVariant(models.Model):
    product = models.ForeignKey(Product)
    color = models.CharField(max_length=80)
