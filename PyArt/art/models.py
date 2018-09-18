from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Art(models.Model):
    """model for art uploads"""
    user = models.ForeignKey(User, related_name='arts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, max_length=255)
    requests = models.ManyToManyField(User, through='Request')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """creates slug and saves model"""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('art:detail', kwargs={'slug':self.slug})

class Request(models.model):
    user = models.ForeignKey(User, related_name='requesting_user' on_delete=models.CASCADE)
    art = models.ForeignKey(Art, related_name='requested_art', on_delete=models.CASCADE)
    message = models.TextField(blank=True, default='')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user','art')