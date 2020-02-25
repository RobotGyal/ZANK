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
from django.contrib import messages


def home(request):
    '''Render the home page of the site.'''
    template_name = 'codes/home.html'
    return render(request, template_name)


class CodeList(ListView):
    '''For showing the reference of all codes, or just ones based on search.'''
    model = Code
    template_name = 'codes/results.html'

    def get(self, request):
        ''' Get a list of all codes currently in the database.'''
        codes = self.get_queryset().all()
        return render(request, self.template_name, {
            'codes': codes
        })


class CodeDetail(DetailView):
    '''For showing the details of a specific Code.'''
    model = Code
    template_name = 'codes/details.html'

    def get(self, request, slug):
        """Renders a page to show a specific code in full detail.
           Parameters:
           slug(slug): specific slug of the Code instance.
           request(HttpRequest): the HTTP request sent to the server

           Returns:
           render: a page of the Code

         """
        code = get_object_or_404(Code, slug__iexact=self.kwargs['slug'])
        code = self.get_queryset().get(slug__iexact=slug)
        context = {
            'code': code
        }
        return render(request, self.template_name, context)

# class CodeUpdate(UpdateView):
#     model = Code
#     form_class = CodeForm
#     template_name = 'codes/crud/update.html'

#     def form_valid(self, form):
#         form.instance.code = self.request.get('title')
#         return super().form_valid(form)

class CodeCreate(UserPassesTestMixin, CreateView):
    '''For adding new Code instances to the db.'''
    model = Code
    form_class = CodeForm
    template_name = 'codes/crud/create.html'
    queryset = Code.objects.all()

    def form_valid(self, form):
        '''Initializes the post_by field based on who submitted the form.'''
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def post(self, request):
        ''' indicate whenever a post request was made. saving '''

        form = CodeForm(request.POST)
        if form.is_valid():
            new_code = form.save(commit=False)
            new_code.post_by = User.objects.get(id=request.user.id)
            new_code.save()
            # return HttpResponseRedirect(reverse('details', args=[new_code.slug]))
        return render(request, 'codes/details.html')



    def get(self, request):
        '''displaying'''


        context = {'form': CodeForm()}

        return render(request, self.template_name, context)

    def test_func(self):
        '''Ensures the user adding the Code is an officer.'''
        # code = self.get_object()
        user = self.request.user
        return (user.is_authenticated is True and
                user.architectorofficer.is_officer is True)


class CodeUpdate(UserPassesTestMixin, UpdateView):
    '''For making changes to existing Code instances.'''
    model = Code
    form_class = CodeForm
    template_name = 'codes/crud/update.html'
    queryset = Code.objects.all()

    def test_func(self):
        '''Ensures the user adding the Code is an officer.'''
        code = self.get_object()
        user = self.request.user
        return (user.is_authenticated is True and
                user.architectorofficer.is_officer is True)



class CodeDelete(LoginRequiredMixin, DeleteView):
    '''For removing Code instances from the db.'''
    model = Code
    # template_name = 'codes/crud/delete.html'
    template_name = 'codes/crud/delete.html'
    success_url = reverse_lazy('codes:reference')
    success_message = "code successfully deleted"
    queryset = Code.objects.all()

    def test_func(self):
        '''Ensures the user adding the Code is an officer.'''
        code = self.get_object()
        user = self.request.user
        return (user.is_authenticated is True and
                user.architectorofficer.is_officer is True)

    def get(self, request, slug):
        '''displaying'''
        code = self.get_queryset().get(slug=slug)

        context = {
            'code': code
        }
        return render(request, self.template_name, context)

    # def delete(self, request, *args, **kwargs):
    #     messages.success(request, self.success_message)
    #     return super().delete(request)

    # def post(self, request, slug):
    #     code = self.get_queryset().get(slug__iexact=slug)
    #     code.delete()
    #     return render(request, 'codes/home.html')
