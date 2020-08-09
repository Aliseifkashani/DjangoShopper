from json import JSONEncoder
from django.http import HttpResponse
import ast
from rest_framework.authtoken.models import Token

from prof.models import User


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def direct(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    if not User.objects.filter(username=body['username']):
        user = User(username=body['username'], password=body['password'], asset=0)
        user.save()
        user.token = str(Token.objects.create(user=user))
        return HttpResponse(MyEncoder().encode(user.token))
    else:
        if body['password'] == User.objects.get(username=body['username']).password:
            user = User.objects.get(username=body['username'], password=body['password'])
            user.token = str(Token.objects.get(user=user).generate_key())
            return HttpResponse(MyEncoder().encode(user.token))
        else:
            return HttpResponse(MyEncoder().encode({'error_message': 'invalid password!'}))


def logout(request): # implemented with token
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    # user_id = body['user_id']
    # user = User.objects.get(id=user_id)
    token = body['token']
    user = Token.objects.get(key=token).user
    Token.objects.get(key=token).delete()
    user.token = None
    return HttpResponse(MyEncoder().encode('Successful logout!'))
