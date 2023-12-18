from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView

from . import models

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/sign_up.html'

class CustomUserDetail(DetailView,LoginRequiredMixin):
    model = models.CustomUser

class CustomUserUpdate(UpdateView,LoginRequiredMixin):
    login_url = '/login/'
    
    fields = ('first_name','last_name','address','phone_no')
    model = models.CustomUser
    success_url = reverse_lazy('home')



