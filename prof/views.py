import ast
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

from nilva.general import request_decorator


@request_decorator
def profile(request):
    user = Token.objects.get(key=request.headers['Authorization'].replace('token', '', 1)).user
    properties = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
        'asset': user.asset,
        'purchased': user.purchased,
        'picture': user.picture.path  # Is it correct to passing the path?
    }
    return JsonResponse(properties, safe=False)


@request_decorator
def update(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    user = Token.objects.get(key=request.headers['Authorization'].replace('token', '', 1)).user
    if 'first_name' in body:
        user.first_name = body['first_name']
    if 'last_name' in body:
        user.last_name = body['last_name']
    if 'username' in body:
        user.username = body['username']
    if 'password' in body:
        user.password = body['password']
    if 'email' in body:
        user.email = body['email']
    if 'asset' in body:
        user.username = int(body['asset'])
    if 'picture' in body:
        user.picture.path = body['picture']  # Is it corrct?
    user.save()
    properties = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
        'asset': user.asset,
        'purchased': user.purchased,
        'picture': user.picture
    }
    return JsonResponse(properties, safe=False)
