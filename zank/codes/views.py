from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from .models import Code
from django.contrib.auth.models import User
from .forms import CodeForm
import zank


def home(request):
    '''Render the home page of the site.'''
    pass


class CodeList(ListView):
    '''For showing the reference of all codes, or just ones based on search.'''
    pass


class CodeDetail(DetailView):
    '''For showing the details of a specific Code.'''
    pass


class CodeCreate(UserPassesTestMixin, CreateView):
    '''For adding new Code instances to the db.'''
    pass


class CodeUpdate(UserPassesTestMixin, UpdateView):
    '''For making changes to existing Code instances.'''
    pass


class CodeDelete(LoginRequiredMixin, DeleteView):
    '''For removing Code instances from the db.'''
    pass
