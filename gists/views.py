
from typing import cast

from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Gist


class GistsListView(ListView):
    model = Gist
    template_name = 'gists/gists_list.html'
    context_object_name = 'gists'


class GistDetailView(LoginRequiredMixin, DetailView):
    model = Gist
    template_name = 'gists/gist_detail.html'


class GistCreateView(LoginRequiredMixin, CreateView):
    model = Gist
    template_name = 'gists/gist_create.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        gist = getattr(self, 'object', None)
        if gist is None:
            return reverse('gists_list')
        return reverse('gist_detail', kwargs={'pk': gist.pk})


class GistUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gist
    template_name = 'gists/gist_update.html'
    fields = ['title', 'body']

    def test_func(self):
        gist = cast(Gist, self.get_object())
        return self.request.user == gist.author


class GistDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gist
    template_name = 'gists/gist_delete.html'
    success_url = reverse_lazy('gists_list')

    def test_func(self):
        gist = cast(Gist, self.get_object())
        return self.request.user == gist.author
