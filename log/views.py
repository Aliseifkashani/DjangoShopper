from django.http import JsonResponse
import ast
from rest_framework.authtoken.models import Token

from prof.models import User
from nilva.general import request_decorator


@request_decorator
def direct(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    if not User.objects.filter(username=body['username']):
        user = User(username=body['username'], password=body['password'], asset=0)
        user.save()
        Token.objects.create(user=user)
        # return HttpResponse(MyEncoder().encode(str(Token.objects.get(user=user))))
        # data = serializers.serialize('json', Token.objects.get(user=user).key)
        return JsonResponse(Token.objects.get(user=user).key, safe=False)
    else:
        if body['password'] == User.objects.get(username=body['username']).password:
            user = User.objects.get(username=body['username'], password=body['password'])
            Token.objects.get(user=user).delete()
            Token.objects.create(user=user)
            return JsonResponse(Token.objects.get(user=user).key, safe=False)
        else:
            return JsonResponse('invalid password!', safe=False)


@request_decorator
def indirect(request):
    pass


@request_decorator
def logout(request):
    token = request.headers['Authorization'].replace('token', '', 1)
    Token.objects.get(key=token).delete()
    return JsonResponse('Successful logout!', safe=False)


def test(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    from django.core import serializers
    import json

    # data = serializers.serialize("json", User.objects.get(username='fammmmjmm').username)
    data = JsonResponse(User.objects.get(username='fammmmjmm'), safe=False)
    return data

