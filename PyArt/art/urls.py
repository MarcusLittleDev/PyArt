from django.urls import path, include
from . import views

app_name = 'art'

urlpatterns = [
    path('', views.ArtList.as_view(), name='gallery'),
    path('upload/', views.UploadArt.as_view(), name='upload'),
    path('<slug:slug>/', views.ArtDetail.as_view(), name='detail')
]