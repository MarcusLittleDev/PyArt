from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Art(models.Model):
    """model for art uploads"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    out_of_stock = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="art/", blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """creates slug and saves model"""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('art:detail', kwargs={'slug':self.slug})