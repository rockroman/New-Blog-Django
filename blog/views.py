from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    { 
        'author': 'roman RR',
        'title': 'blog post 1',
        'content': 'first post created',
        'date_posted': '29 th november 2022'
    },

    { 
        'author': 'mark RR',
        'title': 'blog post 2',
        'content': 'second post created',
        'date_posted': '9 th november 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About us'})