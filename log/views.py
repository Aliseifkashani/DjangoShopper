import ast
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

from prof.models import User
from nilva.general import request_decorator, all_tokens


@request_decorator
def direct(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    if not User.objects.filter(username=body['username']):
        user = User(username=body['username'], password=body['password'], asset=0)
        user.save()
        Token.objects.create(user=user)
        all_tokens.update({Token.objects.get(user=user).key: user.id})
        return JsonResponse(Token.objects.get(user=user).key, safe=False)
    else:
        if body['password'] == User.objects.get(username=body['username']).password:
            user = User.objects.get(username=body['username'], password=body['password'])
            try:
                del all_tokens[Token.objects.get(user=user).key]
                Token.objects.get(user=user).delete()
            except Exception:
                pass
            Token.objects.create(user=user)
            all_tokens.update({Token.objects.get(user=user).key: user.id})
            return JsonResponse(Token.objects.get(user=user).key, safe=False)
        else:
            return JsonResponse('invalid password!', safe=False)


@request_decorator
def logout(request):
    token = request.headers['Authorization'].replace('Token ', '', 1)
    Token.objects.get(key=token).delete()
    return JsonResponse('Successful logout!', safe=False)


def test(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    token = request.headers['Authorization'].replace('Token ', '', 1)
    user = User.objects.get(id=all_tokens[token])
    return JsonResponse(user.asset, safe=False)


