from rest_framework import serializers
from . import models

class ArtSerializer(serializers.ModelSerializer):
    """A serializer for uploading art to the site"""

    class Meta:
        model = models.Art
        fields = ("__all__")