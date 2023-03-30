from django.shortcuts import render
from .models import Post, PostLike, PostTag
from user.models import FriendUser, User
from .forms import AddLikePost
from django.http import JsonResponse, HttpResponse


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
    if request.POST:
        if 'search' in request.POST and request.POST['search']:
            search= request.POST['search']
            search(request, search)

    try:
        id_user = request.user.id
    except:
        id_user = None

    posts = Post.objects.all().filter(active=True).order_by('-date_add')[0:20]
    for post in posts:
        post.check = post.check_like_user(id_user)
    if id_user:
        context = {
            'posts': posts,
            'id_user': id_user,
        }
    else:
        context = {
            'posts': posts,
        }
    return render(request, 'main/index.html', context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def post_add_like(request):
    if is_ajax(request=request):
        post = request.POST['post']
        user = request.POST['user']

        formAddLikePost = AddLikePost(request.POST)
        print(formAddLikePost)
        if formAddLikePost.is_valid():
            formAddLikePost.save()
            quantity = PostLike.objects.filter(post__id=post).count()
            return JsonResponse({"quantity": quantity}, status=200)
        else:
            errors = formAddLikePost.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)


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

