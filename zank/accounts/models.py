from django.db import models
from django.contrib.auth.models import User
from zank import settings
from django.urls import reverse
from django.conf import settings


class ArchitectOrOfficer(models.Model):
    '''A specific type of User - may be a government official or architect.'''
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    is_officer = models.BooleanField(help_text="How will you use ZANK?", default=False)

    def __str__(self):
        '''Return the related User's username.'''
        type = "Officer" if self.is_officer is True else "Architect"
        return f"{self.user.username} the {type}"

    """
    def get_absolute_url(self):
        '''Returns a fully qualified path for user profile.'''
        path_components = {'pk': self.user.id}
        return reverse('accounts:user_info', kwargs=path_components)
    """
