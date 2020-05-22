from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
import json

from .models import User


def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'profile/profile.html', {'user': user})


def update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'profile/update.html', {'user': user})


def apply(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        new_first_name = request.POST['firstName']
        new_last_name = request.POST['lastName']
        new_email = request.POST['email']
        new_asset = int(request.POST['asset'])
        if new_asset == '' or new_email == '' or new_last_name == '' or new_first_name == '':
            raise Exception()
    except Exception:
        return render(request, 'profile/update.html', {
            'user': user,
            'error_message': "You didn't select a text.",
        })
    else:
        user.firstName = new_first_name
        user.lastName = new_last_name
        user.email = new_email
        user.asset = new_asset
        user.save()
    # return HttpResponseRedirect(reverse('profile:profile', args=(user.id,)))
    return json.dumps(user)
