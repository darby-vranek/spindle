from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from . import models


def home_page(request):
    return render(request, 'home_page.html')


def character_detail_page(request):
    return render(request, 'character_detail_page.html')


def character_create_page(request):
    return render(request, 'character_form_page.html')


def character_update_page(request):
    return render(request, 'character_form_page.html')


def character_list_page(request):
    return render(request, 'character_list_page.html')


class PostCreateView(CreateView):
    model = models.Post
    form_class = models.PostForm
    template_name = 'post_form_page.html'
    success_url = reverse_lazy('post-list')


class PostDeleteView(DeleteView):
    model = models.Post
    success_url = reverse_lazy('post-list')
    

class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post_detail_page.html'


class PostUpdateView(UpdateView):
    model = models.Post
    form_class = models.PostForm
    template_name = 'post_form_page.html'
    success_url = reverse_lazy('post-list')


class PostListView(ListView):
    model = models.Post
    template_name = 'post_list_page.html'


# ===== verses =====


class VerseCreateView(CreateView):
    model = models.Verse
    form_class = models.VerseForm
    template_name = 'form_page.html'
    success_url = reverse_lazy('verse-list')


class VerseDeleteView(DeleteView):
    model = models.Verse
    success_url = reverse_lazy('verse-list')


class VerseDetailView(DetailView):
    model = models.Verse
    template_name = 'verse_detail_page.html'


class VerseListView(ListView):
    model = models.Verse
    template_name = 'verse_list_page.html'


class VerseUpdateView(UpdateView):
    model = models.Verse
    form_class = models.VerseForm
    template_name = 'form_page.html'
    success_url = reverse_lazy('verse-list')
