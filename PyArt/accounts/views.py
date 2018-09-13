from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from . import forms
from . import models

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

class ProfileView(LoginRequiredMixin,UpdateView ):
    login_url = '/accounts/login/'
    model = models.User
    form_class = forms.UpdateProfileForm
    template_name = 'accounts/accounts_detail.html'
    success_url = reverse_lazy('accounts:profile',
                                kwargs={ 'username':get_user_model().username})

    def get_object(self):
        return self.request.user

    # def get_form_kwargs(self):
    #     kwargs = super(ProfileView, self).get_form_kwargs()
    #     kwargs.update({'user':self.request.user})
    #     return {'user':self.request.user}
