from django import forms
from .models import Code


class CodeForm(forms.ModelForm):
    '''A form to handle creating and updating Codes.'''
    class Meta:
        model = Code
        exclude = [
            'slug',
            'date_posted',
            'last_revised',
            'posted_by'
        ]
