from django.contrib import auth
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render_to_response
from django.template.context_processors import csrf


def registration(request):
    args = {}
    args.update(csrf(request))

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')

        if username.strip() == '':
            args['loginerror'] = 'Имя не может быть пустым'
            return render_to_response('registration.html', args)
        if password.strip() == '':
            args['loginerror'] = 'Пароль не может быть пустым'
            return render_to_response('registration.html', args)
        if email.strip() == '':
            args['loginerror'] = 'Email не может быть пустым'
            return render_to_response('registration.html', args)
        if password != password2:
            args['loginerror'] = 'Пароли должны совпадать'
            return render_to_response('registration.html', args)
        try:
            User.objects.create_user(username=username, password=password, email=email)
        except IntegrityError:
            args['loginerror'] = 'Пользователь с таким логином уже существует'
            return render_to_response('registration.html', args)

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/shop/')
    else:
        return render_to_response('registration.html', args)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/shop/')
        else:
            args['loginerror'] = 'Пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/shop/')
