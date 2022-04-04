from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    tert='qwert'

    posts = Post.objects.all()
    context = {
        'posts': posts,
        'tert': tert,
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')

