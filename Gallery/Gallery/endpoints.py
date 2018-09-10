from rest_framework.routers import DefaultRouter

from accounts import views as accountviews
from art import views as artviews
from django.urls import include, path

from knox import views as knox_views

router = DefaultRouter()

router.register('profile', accountviews.UserProfileViewSet)
router.register('art', artviews.ArtViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', accountviews.LoginView.as_view(), name='login')
]