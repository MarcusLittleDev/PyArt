from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('art', views.ArtViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
