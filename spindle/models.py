from django.db import models
from django.forms import ModelForm, HiddenInput, Textarea, TextInput
from django_quill.fields import QuillField


class Model(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True

# ===== posts =====


class Post(Model):
    title = models.CharField(max_length=100, default="Untitled")
    content = QuillField()
    comments = models.TextField(blank=True)
    tags = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def tag_list(self):
        return self.tags.split(',')


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
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
                'class': 'form-control tagsinput',
                'data-color': 'dark',
                'placeholder': "tag1, tag2, tag3"
            }),
        }


# ===== verses =====


class Verse(Model):
    name = models.CharField(max_length=50)
    franchise = models.CharField(max_length=50)

    def __str__(self):
        return f'Verse: {self.name}'


class VerseForm(ModelForm):
    class Meta:
        model = Verse
        fields = ['name', 'franchise']
