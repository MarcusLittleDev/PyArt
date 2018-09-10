from django.shortcuts import render

from rest_framework import status, viewsets, filters
from . import models, serializers

# Create your views here.

class ArtViewSet(viewsets.ModelViewSet):
    """Handles creating, deleting, and updating art"""
    serializer_class = serializers.ArtSerializer
    queryset = models.Art.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')