from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator

from . import models
from profile.models import User


def index(request):
    return render(request, 'login/login.html')


def login_direct(request):
    if not User.objects.filter(email=request.POST['email']):
        user = User(email=request.POST['email'], password=request.POST['password'], asset=0)
        user.save()
        user.last_login = default_token_generator.make_token(user)
        return user.last_login
    else:
        if request.POST['password'] == User.objects.get(email=request.POST['email']).password:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
            return user.last_login
        else:
            return render(request, 'login/login.html', {'error_message': 'invalid password'})
