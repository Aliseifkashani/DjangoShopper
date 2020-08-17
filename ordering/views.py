import ast
from django.core import serializers
from django.http import JsonResponse

from .models import Commidity
from prof.models import User
from nilva.general import request_decorator, all_tokens


@request_decorator
def view_products(request):
    data = serializers.serialize('json', Commidity.objects.all())
    return JsonResponse(data, safe=False)


@request_decorator
def buy(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    sum = 0
    for product_id in body['product_ids']:
        sum += Commidity.objects.get(id=product_id).price
    # user = Token.objects.get(key=request.headers['Authorization'].replace('Token ', '', 1)).user
    token = request.headers['Authorization'].replace('Token ', '', 1)
    user = User.objects.get(id=all_tokens[token])
    if sum > user.asset:
        return JsonResponse('no enough money to buy those!', safe=False)
    user.asset -= sum
    for product_id in body['product_ids']:
        commidity = Commidity.objects.get(id=product_id)
        commidity.number -= 1
    user.save()
    return JsonResponse('Successful purchase', safe=False)
