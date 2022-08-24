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
from django.urls import path
from spindle import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('characters/', views.character_list_page, name='character-list'),
    path('characters/new/', views.character_create_page, name='character-create'),
    path('characters/<slug:pk>/', views.character_detail_page, name='character-detail'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('verses/', views.VerseListView.as_view(), name='verse-list'),
    path('verses/new/', views.VerseCreateView.as_view(), name='verse-create'),
    path('verses/<int:pk>/', views.VerseDetailView.as_view(), name='verse-detail'),
    path('verses/<int:pk>/edit/', views.VerseUpdateView.as_view(), name='verse-update'),
    path('verses/<int:pk>/delete/', views.VerseDeleteView.as_view(), name='verse-delete'),
]
