from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, Textarea, TextInput
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
    bio = models.TextField(blank=True)
    avatar = models.URLField(default='', blank=True)
    big_portrait = models.URLField(default='', blank=True)

    def __str__(self):
        return f'{self.name} ({self.page_name})'

    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'page_name': self.page_name})


class Post(Model):
    title = models.CharField(max_length=100, default="Untitled")
    verse = models.ForeignKey('Verse', related_name='posts', on_delete=models.DO_NOTHING, null=True, blank=True)
    content = QuillField()
    comments = models.TextField(blank=True)
    tags = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def tag_list(self):
        return self.tags.split(',')


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


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'verse', 'content', 'comments', 'tags']
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
