from django.shortcuts import get_object_or_404
from json import JSONEncoder

from .models import User


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user
    }
    return MyEncoder().encode(context)


def update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # return render(request, 'profile/update.html', {'user': user})
    context = {
        'user': user
    }
    return MyEncoder().encode(context)


def apply(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
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
    else:
        user.email = new_email
        user.password = new_password
        user.asset = new_asset
        user.save()
    context = {
        'user': user
    }
    return MyEncoder().encode(context)

