from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth import get_user_model

from . import models, forms
# Create your views here.

User = get_user_model()

class UploadArt(LoginRequiredMixin, generic.CreateView):
    model = models.Art
    form_class = forms.ArtUploadForm

    def form_valid(self, form):
        self.object= form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ArtDetail(generic.DetailView):
    model = models.Art

class ArtList(generic.ListView):
    model = models.Art
    context_object_name = 'art'