from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

import uuid

User = get_user_model()
# Create your models here.
class Art(models.Model):
    """model for art uploads"""
    user = models.ForeignKey(User, related_name='arts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, max_length=255)
    taking_request = models.BooleanField(blank=True, default=False)

        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """creates slug and saves model"""
        self.slug = slugify(self.name + '_' + uuid.uuid4().hex)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('art:detail', kwargs={'slug':self.slug})

class Request(models.Model):
    user = models.ForeignKey(User, related_name='requesting_user', on_delete=models.CASCADE)
    art = models.ForeignKey(Art, related_name='requested_art', on_delete=models.CASCADE)
    message = models.TextField(blank=True, default='')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user','art')


def user_directory_path(instance, filename):
    return f'images/user_{instance.art.user.id}/{uuid.uuid4().hex}.png'

class Picture(models.Model):
    art = models.ForeignKey(Art, related_name='art_picture', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=user_directory_path)
    art_thumbnail = ImageSpecField(source='picture', processors=[ResizeToFill(400, 250)],
                                    format='JPEG',
                                    options={'quality':85})

    def __str__(self):
        return self.art.name