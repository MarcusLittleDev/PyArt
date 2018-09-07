from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.permissions import IsAuthenticated

from knox.models import AuthToken
from knox.auth import TokenAuthentication

from . import models, serializers

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, deleting, and updating profiles"""

    serializer_class = serializers.CreateUserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')
    
