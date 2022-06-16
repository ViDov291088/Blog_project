from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    """добавляем функционал для индивидуальных страниц блога"""
    model = Post
    template_name = 'post_detail.html'
