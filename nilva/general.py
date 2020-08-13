from json import JSONEncoder
import ast
from rest_framework.authtoken.models import Token
from django.http import HttpResponse

from prof.models import User


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
                    error = {'error': 'invalid authorization format!'}
                    return HttpResponse(MyEncoder().encode(error))
                if not Token.objects.filter(key=request.headers['Authorization']):
                    return HttpResponse('Unauthorized', status=401)
        if 'username' in body:
            if body['username'] is None or body['username'] == '' and func.__name__ in ['direct', 'update']:
                error = {'error': 'empty username!'}
                return HttpResponse(MyEncoder().encode(error))
            if not User.objects.filter(username=body['username']) and func.__name__ not in ['direct', 'update']:
                error = {'error': 'invalid username!'}
                return HttpResponse(MyEncoder().encode(error))
        if 'password' in body:
            if body['password'] is None or body['password'] == '' and func.__name__ in ['direct', 'update']:
                error = {'error': 'empty password!'}
                return HttpResponse(MyEncoder().encode(error))
            if not User.objects.filter(password=body['password']) and func.__name__ not in ['direct', 'update']:
                error = {'error': 'invalid password!'}
                return HttpResponse(MyEncoder().encode(error))
        if 'user_id' in body:
            # if body['user_id'] is None or body['user_id'] == '':
            #     error = {'error': 'empty user_id!'}
            #     return HttpResponse(MyEncoder().encode(error))
            if not User.objects.filter(user_id=body['user_id']) and func.__name__ != 'update':
                error = {'error': 'invalid user_id!'}
                return HttpResponse(MyEncoder().encode(error))
        if 'email' in body:
            if body['email'] is None or body['email'] == '' and func.__name__ == 'update':
                error = {'error': 'empty email!'}
                return HttpResponse(MyEncoder().encode(error))
            if not User.objects.filter(email=body['email']) and func.__name__ != 'update':
                error = {'error': 'invalid email!'}
                return HttpResponse(MyEncoder().encode(error))
        if 'product_ids' in body:
            if len(body['product_ids'] == 0):
                error = {'error': 'empty shopping cart!'}
                return HttpResponse(MyEncoder().encode(error))
        return func(request)
    return check
