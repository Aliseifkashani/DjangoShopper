from json import JSONEncoder
import ast
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse

from ordering.models import Commidity
from prof.models import User

all_tokens = {}


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def request_decorator(func):
    def check(request):
        dict_str = request.body.decode("UTF-8")
        body = ast.literal_eval(dict_str)
        if 'Authorization' in request.headers and func.__name__ != 'direct':
            if not (request.headers['Authorization'] is None or request.headers['Authorization'] == ''):
                if not request.headers['Authorization'].startswith('Token '):
                    return JsonResponse('invalid authorization format!', safe=False)
                if not Token.objects.filter(key=request.headers['Authorization'].replace('Token ', '', 1)):
                    return HttpResponse('Unauthorized', status=401)
        if 'username' in body:
            if body['username'] is None or body['username'] == '' and func.__name__ in ['direct', 'update']:
                return JsonResponse('empty username!', safe=False)
            if not User.objects.filter(username=body['username']) and func.__name__ not in ['direct', 'update']:
                return JsonResponse('invalid username!', safe=False)
        if 'password' in body:
            if body['password'] is None or body['password'] == '' and func.__name__ in ['direct', 'update']:
                return JsonResponse('empty password!', safe=False)
            if not User.objects.filter(password=body['password']) and func.__name__ not in ['direct', 'update']:
                return JsonResponse('invalid password!', safe=False)
        if 'user_id' in body:
            # if body['user_id'] is None or body['user_id'] == '':
            #     error = {'error': 'empty user_id!'}
            #     return HttpResponse(MyEncoder().encode(error))
            if not User.objects.filter(user_id=body['user_id']) and func.__name__ != 'update':
                return JsonResponse('invalid user_id!', safe=False)
        if 'email' in body:
            if body['email'] is None or body['email'] == '' and func.__name__ == 'update':
                return JsonResponse('empty email!', safe=False)
            if not User.objects.filter(email=body['email']) and func.__name__ != 'update':
                return JsonResponse('invalid email!', safe=False)
        if 'product_ids' in body:
            if len(body['product_ids']) == 0:
                return JsonResponse('empty shopping cart!', safe=False)
            for product_id in body['product_ids']:
                if not Commidity.objects.filter(id=product_id):
                    return JsonResponse('invalid product (id)!', safe=False)
                if Commidity.objects.get(id=product_id).number <= 0:
                    return JsonResponse('inadequate amount of this commidity!', safe=False)
        return func(request)
    return check
