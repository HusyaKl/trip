from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from markupsafe import re
from .models import Account
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
import django



def create_user(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    Account.objects.create_user(email, username, password)
    return HttpResponse('200')

def sign_in(request):
    email = request.POST['email']
    password = request.POST['password']
    user = auth.authenticate(request, email=email, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponse('200')
    else:
        return HttpResponse('404')

def current_user(request):
    if not request.user.is_authenticated:
        return JsonResponse({'username': False})
    user = request.user
    data = {}
    return JsonResponse({
        'username': user.username
    })
@csrf_exempt
def logout(request):
    auth.logout(request)
    return HttpResponse('200')

@csrf_exempt
def csrftoken(request):
    if request.POST.get('key') == 'MdEy9qM)<?HFHSE?``9h}d1)$AbyQSU%AP]~I%+C>wKS^kkPN%,@S^PDlhoKF&B':
        response = {
            'csrfmiddlewaretoken': django.middleware.csrf.get_token(request),
        }
        return JsonResponse(response)
    else:
        return HttpResponse('403')
