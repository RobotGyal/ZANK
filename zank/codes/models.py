from django.db import models
from accounts.models import ArchitectOrOfficer
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy


class Code(models.Model):
    '''Represents one section of the building code.'''
    title = models.CharField(max_length=60, help_text="Code title.")
    slug = models.CharField(max_length=60,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this code." +
                                      "Computer Generated.")
    description = models.TextField(help_text="Full text of the code.")
    date_posted = models.DateTimeField(auto_now_add=True, help_text=(
            "The date and time this page was created. " +
            "Automatically generated when the model saves.")
        )
    last_revised = models.DateTimeField(auto_now=True, help_text=(
        "The date and time this page was updated. " +
        "Automatically generated when the model updates.")
    )
    posted_by = models.OneToOneField(settings.AUTH_USER_MODEL,blank=True, null=True,
                                     on_delete=models.PROTECT
                                     )
    can_dos = models.TextField(
        help_text="List of do's associated with this code.")
    cannot_dos = models.TextField(
        help_text="List of don'ts associated with this code.")
    
    is_visible = models.BooleanField(help_text="Code officially active?", default=True)

    def __str__(self):
        '''Return the title of the Code for presentation purposes.'''
        return self.title

    def save(self, *args, **kwargs):
        '''Creates a URL safe slug automatically when a new code is made.'''
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # call save on the superclass
        return super(Code, self).save(*args, **kwargs)

    def get_absolute_url(self):
        '''Returns a fully qualified path for building code instance.'''
        path_components = {'slug': self.slug}
        return reverse('codes:details', kwargs=path_components)