from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import django.contrib.auth.forms as auth_forms

# credit for subclassing UserCreationForm belongs to
# https://overiq.com/django-1-10/django-creating-users-using-usercreationform/


class SignUpForm(UserCreationForm):
    '''A form that handles registering new users.'''
    class Meta:
        model = User
        fields = ['email', 'username',
                  'first_name', 'last_name',
                  'password1', 'password2'
                  ]

    def save(self, commit=True):
        '''Initializes fields of the new User instance.'''
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit is True:
            user.save()

        return user
