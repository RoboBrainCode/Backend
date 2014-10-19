from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django import forms
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from base64 import b64decode


@ensure_csrf_cookie
def create_user_rb(request):
  if request.method == 'GET':
    return HttpResponse('Ok')
  elif request.method == 'POST':
    payload = json.loads(request.body)
    username = payload['username']
    email = payload['email']
    password = payload['password']
    if email and User.objects.filter(email=email).exclude(username=username).count():
      return HttpResponse('This email address is already in use! Try logging in.', status=401)
    if email and User.objects.filter(email=email, username=username).count():
      return HttpResponse('This account already exists! Try logging in.', status=401)
    user = User.objects.create_user(username, email, password)
    user.save()
    return HttpResponse('Ok')

@ensure_csrf_cookie
def login_rb(request):
  if request.user.is_authenticated():
    user = request.user
    user_data = {
      'id': user.id,
      'username': user.username,
      'email': user.email,
      'loggedin': 'True'
    };
    return HttpResponse(json.dumps(user_data), content_type='application/json')
  if request.method == 'GET':
    return HttpResponse('Ok')
  elif request.method == 'POST':
    decodedCredentials = b64decode(request.body)
    if not ':' in decodedCredentials:
      return HttpResponse('Not logged in', status=401)
    email, password = decodedCredentials.split(':')
    user = authenticateEmail(email, password)
    if not user:
      return HttpResponse('Invalid Credentials', status=401)
    user = authenticate(username=user.username, password=password)
    if not user:
      return HttpResponse('Invalid Credentials', status=401)
    login(request, user)

    user_data = {
      'id': user.id,
      'username': user.username,
      'email': user.email
    };
    return HttpResponse(json.dumps(user_data), content_type='application/json')

def authenticateEmail(email=None, password=None):
  try:
      user = User.objects.get(email=email)
      if user.check_password(password):
          return user
  except User.DoesNotExist:
      return None

def logout_rb(request):
  logout(request)
  return HttpResponse('Logged Out')
