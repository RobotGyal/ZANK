from django.shortcuts import render
from accounts.forms import SignUpForm
from .models import ArchitectOrOfficer
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.views.generic.detail import (DetailView)
from django.views.generic.edit import (
    CreateView
    # UserProfile
)


class SignUpView(SuccessMessageMixin, CreateView):
    '''Allows site visitors to set up a new account as architect or officer.'''
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')  # not implemented yet
    template_name = 'accounts/signup.html'
    success_message = '''Congratulations! You may now log in to Zank. 
                         Please go to your profile to validate your architect/officer status.'''

    def form_valid(self, form):
        '''Save the new User, and set up their profile as well.'''
        self.object = form.save()
        architect_or_officer = ArchitectOrOfficer.objects.create(user=self.object, 
                                                                 is_officer=False)
        architect_or_officer.save()
        return super().form_valid(form)

class UserProfile(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    '''For showing the details of a specific Code.'''
    model = User
    template_name = 'accounts/profile.html'
    queryset = User.objects.all()

    def get(self, request, pk):
        """Renders a page to show a specific user in full detail.
           Parameters:
           pk(pk): specific pk of the User instance.
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page of the User

         """
        # user = get_object_or_404(User, pk=self.kwargs['pk'])
        user = self.queryset.get(id=pk)
        context = {
            'user': user
        }
        return render(request, self.template_name, context)

    def test_func(self):
        '''shows user.'''
        user = self.get_object()
        requesting_user = self.request.user
        return (user.is_authenticated is True and user == requesting_user)
    
#who_is_typing_this_10