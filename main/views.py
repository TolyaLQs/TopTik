from django.shortcuts import render
from .models import Post
from user.models import FriendUser, User

# Create your views here.


def index(request):
    # # if user.authenticated:
    #     posts = Post.objects.all().filter(author=user__friend_user.friend_user__name).order_by('-date_add')
    #     friends = FriendUser.objects.filter(user_friend__name=user.name)
    #     context = {
    #         'posts': posts,
    #         'friends': friends,
    #     }
    # else:
    # user = User.objects.get()
    # user.set_password('1234')
    # user.save()
    posts = Post.objects.all().order_by('-date_add')
    context = {
        'posts': posts,
    }

    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')

