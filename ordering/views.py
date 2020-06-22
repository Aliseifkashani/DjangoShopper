from json import JSONEncoder
from django.http import HttpResponse

from .models import Commidity
from profile.models import User
from login.models import all_tokens


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def view(request):
    try:
        token = request.META['HTTP_AUTHORIZATION'].split(' ', 1)[1]
        if token not in all_tokens:
            raise Exception
        context = {
            'commidities': Commidity.objects.all()
        }
        return MyEncoder().encode(context)
    except Exception:
        return HttpResponse('Unauthorized', status=401)


def buy(request, product_ids):
    try:
        token = request.META['HTTP_AUTHORIZATION'].split(' ', 1)[1]
        if token not in all_tokens:
            raise Exception
    except Exception:
        return HttpResponse('Unauthorized', status=401)
    user_id = all_tokens[token]
    sum = 0
    for product_id in product_ids:
        if not Commidity.objects.filter(id=product_id):
            context = {
                'commidities': Commidity.objects.exclude(number=0),
                'error_message': 'invalid product',
                'user_id': user_id
            }
            return MyEncoder().encode(context)
        sum += Commidity.objects.get(id=product_id)

    if sum > User.objects.get(user_id).asset:
        context = {
            'commidities': Commidity.objects.exclude(number=0),
            'error_message': 'no enough money to buy these',
            'user_id': user_id
        }
        return MyEncoder().encode(context)

    User.objects.get(user_id).asset -= sum
    context = {
        'commidities': Commidity.objects.exclude(number=0),
        'user_id': user_id,
    }
    return MyEncoder().encode(context)
