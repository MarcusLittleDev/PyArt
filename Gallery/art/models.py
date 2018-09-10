from django.db import models

# Create your models here.
class Art(models.Model):
    """model for art uploads"""
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    out_of_stock = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="art/", blank=False)