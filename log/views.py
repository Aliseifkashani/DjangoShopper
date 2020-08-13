from django.http import HttpResponse, JsonResponse
import ast
from rest_framework.authtoken.models import Token

from prof.models import User
from nilva.general import request_decorator, MyEncoder


@request_decorator
def direct(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    if not User.objects.filter(username=body['username']):
        user = User(username=body['username'], password=body['password'], asset=0)
        user.save()
        Token.objects.create(user=user)
        return HttpResponse(MyEncoder().encode(str(Token.objects.get(user=user))))
    else:
        if body['password'] == User.objects.get(username=body['username']).password:
            user = User.objects.get(username=body['username'], password=body['password'])
            Token.objects.get(user=user).delete()
            Token.objects.create(user=user)
            return HttpResponse(MyEncoder().encode(str(Token.objects.get(user=user))))
        else:
            return HttpResponse(MyEncoder().encode({'error': 'invalid password!'}))


@request_decorator
def logout(request):
    token = request.headers['Authorization'].replace('token', '', 1)
    Token.objects.get(key=token).delete()
    return HttpResponse(MyEncoder().encode('Successful logout!'))


def test(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)

    return JsonResponse('User.()')
