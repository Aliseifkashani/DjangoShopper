from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import User


def index(request):
    return render(request, 'profile/index.html', {})


def profile(request, userID):
    user = User.objects.get(id=userID)
    output = ''
    for attribute in dir(user):
        if not '_' in attribute:
            output += attribute + '\n'
    return HttpResponse(output)


def update(request, userID):
    return HttpResponse('to update page')