from json import JSONEncoder

from .models import Commidity
from profile.models import User


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def buy(requset, product_ids, user_id):
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
