from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from . import models
from profile.models import User


def index(request):
    return render(request, 'login/login.html')


def login_direct(request):
    if User.objects.filter(email=request.POST['email']) is None:
        user = User(email=request.POST['email'], password=request.POST['password'])
        user.save()
    else:
        if request.POST['password'] == User.objects.get(email=request.POST['email']).password:
            return default_token_generator.make_token(User.objects.get(email=request.POST['email'], password=request.
                                                                       POST['password']))
        else:
            return render(request, 'login/login.html', {
                'error_message': 'invalid password'
            })
