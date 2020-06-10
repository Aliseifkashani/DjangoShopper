from django.contrib.auth.tokens import default_token_generator
from json import JSONEncoder

from profile.models import User


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def index(request):
    context = {
        'users': User.objects.all()
    }
    return MyEncoder().encode(context)


def login_direct(request):
    if not User.objects.filter(email=request.POST['email']):
        user = User(email=request.POST['email'], password=request.POST['password'], asset=0)
        user.save()
        user.last_login = default_token_generator.make_token(user)
        context = {user.last_login}
        return MyEncoder().encode(context)
    else:
        if request.POST['password'] == User.objects.get(email=request.POST['email']).password:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
            user.last_login = default_token_generator.make_token(user)
            context = {user.last_login}
            return MyEncoder().encode(context)
        else:
            context = {
                'error_message': 'invalid password',
                'users': User.objects.all()
            }
            return MyEncoder().encode(context)


def logout(request, user_id):
    user = User.objects.get(id=user_id)
    user.last_login = None
    context = {
        'user_id': user_id
    }
    return MyEncoder().encode(context)
