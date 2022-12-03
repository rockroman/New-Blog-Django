from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic
# Create your views here.


class home(generic.ListView):
    model = Post
    template_name = 'blog/home.html'

"""
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)"""



def about(request):
    return render(request, 'blog/about.html', {'title': 'About us'})