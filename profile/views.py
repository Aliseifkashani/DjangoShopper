from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from json import JSONEncoder

from .models import User
from login.models import all_tokens


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def profile(request):
    try:
        token = request.META['HTTP_AUTHORIZATION'].split(' ', 1)[1]
        if token not in all_tokens:
            raise Exception
    except Exception:
        return HttpResponse('Unauthorized', status=401)
    # user = get_object_or_404(User, pk=user_id)
    user_id = all_tokens[token]
    context = {
        'user_id': user_id
    }
    return MyEncoder().encode(context)


def update(request):
    # user = get_object_or_404(User, pk=user_id)
    try:
        token = request.META['HTTP_AUTHORIZATION'].split(' ', 1)[1]
        if token not in all_tokens:
            raise Exception
    except Exception:
        return HttpResponse('Unauthorized', status=401)
    user_id = all_tokens[token]
    user = User.objects.get(id=user_id)
    """try:
        new_password = request.POST['password']
        new_email = request.POST['email']
        new_asset = int(request.POST['asset'])
        if new_asset == '' or new_email == '' or new_password == '':
            raise Exception()
    except Exception:
        context = {
            'user': user,
            'error_message': "Some text isn't filled"
        }
        return MyEncoder().encode(context)
    else:"""
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.asset = int(request.POST['asset'])
    user.save()
    context = {
        'user_id': user_id
    }
    return MyEncoder().encode(context)

