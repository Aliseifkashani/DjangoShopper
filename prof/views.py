from django.http import HttpResponse
from json import JSONEncoder

from .models import User


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
    user_id = all_tokens[token]
    context = {
        'user_id': user_id
    }
    return MyEncoder().encode(context)


def update(request):
    try:
        token = request.META['HTTP_AUTHORIZATION'].split(' ', 1)[1]
        if token not in all_tokens:
            raise Exception
    except Exception:
        return HttpResponse('Unauthorized', status=401)
    user_id = all_tokens[token]
    user = User.objects.get(id=user_id)
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.asset = int(request.POST['asset'])
    user.save()
    context = {
        'user_id': user_id
    }
    return MyEncoder().encode(context)

