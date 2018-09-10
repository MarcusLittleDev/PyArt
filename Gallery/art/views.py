from django.shortcuts import render

from rest_framework import status, viewsets, filters, permissions

from . import models, serializers

from knox.auth import TokenAuthentication

# Create your views here.

class ArtViewSet(viewsets.ModelViewSet):
    """Handles creating, deleting, and updating art"""
    serializer_class = serializers.ArtSerializer
    queryset = models.Art.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')

    def get_permissions(self):
        """instantiates and returns the list of permissions that this view requires"""

        if self.action in ['list', 'retrieve']:
            permission_classes = (permissions.AllowAny,)
        else:
            permission_classes = (permissions.IsAdminUser,)

        return [permission() for permission in permission_classes]