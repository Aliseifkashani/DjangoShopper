from django.contrib.auth.tokens import default_token_generator
from json import JSONEncoder
# from django.contrib.auth.backends import BaseBackend

from profile.models import User
from .models import all_tokens


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def login_direct(request):
    if not User.objects.filter(email=request.POST['email']):
        user = User(email=request.POST['email'], password=request.POST['password'], asset=0)
        user.save()
        user.last_login = default_token_generator.make_token(user)
        all_tokens.update({user.last_login: user.id})
        context = {
            'toeken': user.last_login
        }
        return MyEncoder().encode(context)
    else:
        if request.POST['password'] == User.objects.get(email=request.POST['email']).password:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
            del all_tokens[user.last_login]
            user.last_login = default_token_generator.make_token(user)
            all_tokens.update({user.last_login: user.id})
            context = {
                'toeken': user.last_login
            }
            return MyEncoder().encode(context)
        else:
            context = {
                'error_message': 'invalid password',
            }
            return MyEncoder().encode(context)


def logout(request):
    token = request.META['HTTP_AUTHORIZATION'].split(' ', 1)[1]
    user = User.objects.get(id=all_tokens[token])
    user.last_login = None
    context = {
        'user_id': all_tokens[token]
    }
    del all_tokens[token]
    return MyEncoder().encode(context)
