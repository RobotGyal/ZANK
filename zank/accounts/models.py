from django.db import models
from django.contrib.auth.models import User
from explorer import settings
from django.urls import reverse
from django.conf import settings


class ArchitectOrOfficer(models.Model):
    '''A specific type of User - may be a government official or architect.'''
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    def __str__(self):
        '''Return the related User's username.'''
        return f"{self.user.username}"

    """
    def get_absolute_url(self):
        '''Returns a fully qualified path for user profile.'''
        path_components = {'pk': self.user.id}
        return reverse('accounts:user_info', kwargs=path_components)
    """
