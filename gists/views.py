from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Gist

# Create your views here.
class GistsListView(ListView):
    model = Gist
    template_name = 'gists/gists_list.html'
    context_object_name = 'gists'

class GistDetailView(DetailView):
    model = Gist
    template_name = 'gists/gist_detail.html'

class GistCreateView(CreateView):
    model = Gist
    template_name = 'gists/gist_create.html'
    fields = ['title', 'body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('gist_detail', kwargs={'pk': self.object.pk})

class GistUpdateView(UpdateView):
    model = Gist
    template_name = 'gists/gist_update.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class GistDeleteView(DeleteView):
    model = Gist
    template_name = 'gists/gist_delete.html'
    success_url = '/gists/'

