from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from json import JSONEncoder
import json

from .models import User


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'profile/profile.html', {'user': user})


def update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'profile/update.html', {'user': user})


def apply(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        new_password = request.POST['password']
        new_email = request.POST['email']
        new_asset = int(request.POST['asset'])
        if new_asset == '' or new_email == '' or new_password == '':
            raise Exception()
    except Exception:
        return render(request, 'profile/update.html', {
            'user': user,
            'error_message': "You didn't select a text.",
        })
    else:
        user.email = new_email
        user.password = new_password
        user.asset = new_asset
        user.save()
    # return HttpResponse(MyEncoder().encode(user))
    return MyEncoder().encode(user)

