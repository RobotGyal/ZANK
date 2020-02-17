from django.shortcuts import render
from accounts.forms import SignUpForm
from .models import ArchitectOrOfficer
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.views.generic.edit import (
    CreateView
)


class SignUpView(SuccessMessageMixin, CreateView):
    '''Allows site visitors to set up a new account as architect or officer.'''
    pass
