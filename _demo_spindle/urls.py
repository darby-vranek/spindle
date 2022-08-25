"""_demo_spindle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from spindle import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', auth_views.LoginView.as_view(template_name='sign_in.html'), name='sign-in'),
    path('signout/', views.sign_out, name='sign-out'),
    path('', views.home_page, name='home'),
    path('characters/', views.CharacterListView.as_view(), name='character-list'),
    path('characters/new/', views.CharacterCreateView.as_view(), name='character-create'),
    path('characters/<slug:page_name>/', views.CharacterDetailView.as_view(), name='character-detail'),
    path('characters/<slug:page_name>/edit/', views.CharacterUpdateView.as_view(), name='character-update'),
    path('characters/<slug:page_name>/delete/', views.CharacterDeleteView.as_view(), name='character-delete'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('verses/', views.VerseListView.as_view(), name='verse-list'),
    path('verses/new/', views.VerseCreateView.as_view(), name='verse-create'),
    path('verses/<int:pk>/', views.VerseDetailView.as_view(), name='verse-detail'),
    path('verses/<int:pk>/edit/', views.VerseUpdateView.as_view(), name='verse-update'),
    path('verses/<int:pk>/delete/', views.VerseDeleteView.as_view(), name='verse-delete')
]
