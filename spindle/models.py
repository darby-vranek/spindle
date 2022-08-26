from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, Textarea, TextInput, HiddenInput, ModelChoiceField
from django.urls import reverse
from django_quill.fields import QuillField


class Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Character(Model):
    name = models.CharField(max_length=50)
    page_name = models.SlugField(max_length=20, unique=True)
    caption = models.CharField(max_length=30, default='', blank=True)
    bio = QuillField(blank=True)
    avatar = models.URLField(default='', blank=True)
    big_portrait = models.URLField(default='', blank=True)

    class Meta:
        ordering = ['page_name']

    def __str__(self):
        return f'{self.name} ({self.page_name})'

    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'page_name': self.page_name})


class Post(Model):
    title = models.CharField(max_length=100, default="Untitled")
    verse = models.ForeignKey('Verse', related_name='posts', on_delete=models.DO_NOTHING, null=True, blank=True)
    character = models.ForeignKey('Character', related_name='posts', on_delete=models.CASCADE, null=True, blank=True)
    content = QuillField()
    comments = models.TextField(blank=True)
    tags = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def tag_list(self):
        return self.tags.split(',')


class Thread(Model):
    title = models.CharField(max_length=100, default="Untitled")
    characters = models.ManyToManyField('Character', related_name='threads')
    verse = models.ForeignKey('Verse', related_name='threads', on_delete=models.DO_NOTHING, null=True, blank=True)
    comments = models.TextField(blank=True)
    tags = models.TextField(blank=True)

    def __str__(self):
        return f'Thread: {self.title}'

    def last_reply(self):
        return self.replies.latest('created')

    def reply_form(self):
        f = ReplyForm(initial={
            'thread': self
        })
        return f

    def tag_list(self):
        return self.tags.split(',')

    def get_absolute_url(self):
        return reverse('thread-detail', kwargs={'pk': self.pk})


class Reply(Model):
    character = models.ForeignKey('Character', related_name='replies', on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', related_name='replies', on_delete=models.CASCADE)
    content = QuillField()
    comments = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('thread-detail', kwargs={ 'pk': self.thread.pk })


class Verse(Model):
    name = models.CharField(max_length=50)
    franchise = models.CharField(max_length=50, default='', blank=True)

    def get_absolute_url(self):
        return reverse('verse-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Verse: {self.name}'


# ===== forms =====


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'page_name', 'caption', 'bio', 'avatar', 'big_portrait']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'page_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'caption': TextInput(attrs={
                'class': 'form-control'
            }),
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'character', 'verse', 'content', 'comments', 'tags']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
            }),
            'comments': Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'placeholder': 'What\'s on your mind?'
            }),
            'tags': TextInput(attrs={
                'class': 'form-control',
                'data-color': 'dark',
                'placeholder': "tag1, tag2, tag3"
            }),
        }


class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'characters', 'verse', 'comments', 'tags']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
            }),
            'comments': Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'placeholder': 'What\'s on your mind?'
            }),
            'tags': TextInput(attrs={
                'class': 'form-control',
                'data-color': 'dark',
                'placeholder': "tag1, tag2, tag3"
            }),
        }


class VerseForm(ModelForm):
    class Meta:
        model = Verse
        fields = ['name', 'franchise']


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['thread', 'character', 'content', 'comments']
        widgets = {
            'thread': HiddenInput(),
            'comments': Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'placeholder': 'What\'s on your mind?'
            }),
        }

