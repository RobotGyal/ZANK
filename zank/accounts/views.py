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
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')  # not implemented yet
    template_name = 'accounts/signup.html'
    success_message = "Congratulations! You may now log in to Zank"

    def form_valid(self, form):
        '''Save the new User, and set up their profile as well.'''
        self.object = form.save()
        # user = Profile.objects.create(user=self.object)
        # profile.save()
        return super().form_valid(form)
