from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views import View

from . import models


def home_page(request):
    return render(request, 'home_page.html', context={
        'character_list': models.Character.objects.all(),
        'post_list': models.Post.objects.all(),
        'verse_list': models.Verse.objects.all(),
        'thread_list': models.Thread.objects.all(),
        'reply_list': models.Reply.objects.all()
    })


def sign_out(request):
    logout(request)
    return redirect('sign-in')


# ===== characters =====


class CharacterCreateView(CreateView):
    model = models.Character
    form_class = models.CharacterForm
    template_name = 'form_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CharacterDeleteView(DeleteView):
    model = models.Character
    success_url = reverse_lazy('character-list')
    slug_field = 'page_name'
    slug_url_kwarg = 'page_name'


class CharacterDetailView(DetailView):
    model = models.Character
    template_name = 'character_detail_page.html'
    slug_field = 'page_name'
    slug_url_kwarg = 'page_name'


class CharacterListView(ListView):
    model = models.Character
    template_name = 'character_list_page.html'


class CharacterUpdateView(UpdateView):
    model = models.Character
    form_class = models.CharacterForm
    template_name = 'form_page.html'
    slug_field = 'page_name'
    slug_url_kwarg = 'page_name'


# ===== posts =====


class PostCreateView(CreateView):
    model = models.Post
    form_class = models.PostForm
    template_name = 'post_form_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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


class PostListView(ListView):
    model = models.Post
    template_name = 'post_list_page.html'


# ===== threads =====


class ThreadCreateView(CreateView):
    model = models.Thread
    form_class = models.ThreadForm
    template_name = 'post_form_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ThreadDeleteView(DeleteView):
    pass


class ThreadDetailView(DetailView):
    model = models.Thread
    template_name = 'thread_detail_page.html'


class ThreadListView(ListView):
    model = models.Thread
    template_name = 'thread_list_page.html'


class ThreadUpdateView(UpdateView):
    pass


class ReplyCreateView(View):

    def post(self, request, *args, **kwargs):
        form = models.ReplyForm(request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
        return redirect(reverse_lazy('thread-detail', kwargs={'pk': form.instance.thread.pk}))


class ReplyDeleteView(DeleteView):
    model = models.Reply
    success_url = reverse_lazy('thread-list')


class ReplyUpdateView(UpdateView):
    model = models.Reply
    form_class = models.ReplyForm
    template_name = 'post_form_page.html'


# ===== verses =====


class VerseCreateView(CreateView):
    model = models.Verse
    form_class = models.VerseForm
    template_name = 'form_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
