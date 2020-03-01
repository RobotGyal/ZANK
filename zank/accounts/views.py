from django.shortcuts import render
from accounts.forms import SignUpForm
from .models import ArchitectOrOfficer
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import ArchitectOrOfficer
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import (DetailView)
from django.views.generic.edit import (
    CreateView
    # UserProfile
)


class SignUpView(SuccessMessageMixin, CreateView):
    '''Allows site visitors to set up a new account as architect or officer.'''
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
    success_message = (
        '''Congratulations! You may now log in to Zank.
            Please go to your profile to confirm your officer status.'''
        )

    def form_valid(self, form):
        '''Save the new User, and set up their profile as well.'''
        self.object = form.save()
        architect_or_officer = ArchitectOrOfficer.objects.create(
            user=self.object,
            is_officer=False)
        architect_or_officer.save()
        return super().form_valid(form)


class UserProfile(UserPassesTestMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_queryset(self):
        '''Returns a queryset of all User objects.'''
        return self.model.objects.all()

    def get(self, request, pk):
        """Renders a page to show an account of user.
           Parameters:
           pk(int): specific id of the User in db.
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: HttpResponse

         """
        user = self.get_queryset().get(id=pk)
        status = ArchitectOrOfficer.objects.get(user=user)
        context = {
            'user': user
        }
        return render(request, self.template_name, context)

    def test_func(self):
        '''Ensures the user can see only their own profile.'''
        requested_user = self.get_object()
        user = self.request.user
        return requested_user == user
