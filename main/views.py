from django.shortcuts import render
from .models import Post, PostLike, PostTag
from user.models import FriendUser, User

# Create your views here.


def index(request):
    # # if request.user.authenticated:
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
    posts = Post.objects.all().filter(active=True).order_by('-date_add')
    context = {
        'posts': posts,
    }
    return render(request, 'main/index.html', context)


def search(request, search=None):
    if request.method == 'GET':
        if search:
            print('123', search[0])
            posts = PostTag.objects.all().filter(tag__name=search, post__active=True).order_by('-post__date_add')
            if posts:
                context = {
                    'posts': posts,
                }
                return render(request, 'main/search.html', context)
            else:
                error_search = 'То что вы ищите, не найдено |('
                context = {
                    'error_search': error_search,
                }
                return render(request, 'main/search.html', context)
        return render(request, 'main/search.html')


def about(request):
    return render(request, 'main/about.html')

