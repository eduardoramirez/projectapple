from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import json

def user_register(request):
  context = RequestContext(request)

  ret = {'message': ''}

  user_form = UserForm()

  profile_form = UserProfileForm()

  status = str(request.GET.get('from',''))

  if request.user.username != '':
    return HttpResponseRedirect('/')
  if request.method == 'POST':

    # grab data from forms
    user_form = UserForm(data=request.POST)
    profile_form = UserProfileForm(data=request.POST)

    # check for validity then register this user
    if user_form.is_valid() and profile_form.is_valid() and request.POST['username'] != 'anonymous':
      user = user_form.save()
      user.set_password(user.password)
      user.save()

      # this step is required for user's profile
      profile = profile_form.save(commit=False)
      profile.user = user

      # auto-login after register
      new_username = request.POST['username']
      new_password = request.POST['password']
      new_user = authenticate(username=new_username, password=new_password)
      login(request, new_user)
      return HttpResponseRedirect('/')
    ret['message'] = 'Registration Failed' # show register failed message
  
  ret['form'] = {'user': user_form, 'profile': profile_form}
  return render_to_response('register.html', ret, context)

def user_login(request):
  context = RequestContext(request)
  ret = {'message': ''}

  if request.user.username != '':
    return HttpResponseRedirect('/')

  if request.method = 'POST':

    if 'register' in request.POST:
      return HttpResponseRedirect('/register?from=login') 

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if not user:
      ret['message'] = 'Incorrect username or password'
      return render_to_response('login.html', ret, context)

    if user.is_active:
      login(request, user)
      return HttpResponseRedirect('/')

    ret['message'] = 'Account disabled'

  return render_to_response('login.html', ret, context)

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login')

