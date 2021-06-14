from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def first(request):
    return render(request, '1.html')

# Create your views here.

def home(request):
    return render(request, 'home.html')


def information(request):
    return render(request, 'information.html')