from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from user.forms import CreateUserForm, ChangeUserForm, ChangeUserAvatarForm
# Create your views here.
from django.urls import reverse

from user.models import User


def user_login(request):
    if request.POST:
        if 'email' in request.POST and request.POST['email']:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
            else:
                error = 'Не правельно введены данные.'
                context = {
                    'error': error,
                }
                return render(request, 'user/login.html', context)
        elif 'username' in request.POST and request.POST['username']:
            name = request.POST['username']
            user = User.objects.filter(name=name)
            if user:
                error = 'Данное имя занято.'
                context = {
                    'error': error,
                }
                return render(request, 'user/login.html', context)
            else:
                request.session['name'] = name
                return HttpResponseRedirect(reverse('user:register'))

    return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def user_register(request):
    name = request.session.get('name', 'Нет имя')
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            email = request.POST['email']
            password = request.POST['password1']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        register_form = CreateUserForm()
        for reg in register_form:
            if reg.name == 'name':
                reg.initial = name

    context = {
        'register_form': register_form,
        'name': name,
    }
    return render(request, 'user/register.html', context)


def user_edit(request):
    if request.method == 'Post':
        edit_form = ChangeUserForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('user:edit'))
    else:
        edit_form = ChangeUserForm(instance=request.user)

    context = {
        'edit_form': edit_form,
    }
    return render(request, 'user/edit.html', context)


def user_profile(request, id=None):
    pass

