from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
      name = request.user.username
    else:
        return redirect('%s?next=%s' % (reverse('login'), reverse('hello_index'))) 
    return HttpResponse("<h3>Hello, %s</h3>" % name)


def log_in(request):
    if request.method == 'POST':
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'])
        else:
            error = 'Invalid credentials!'
    else: # GET
        error=None
    return HttpResponse(render(request, 'hello/login.html'), {'error': error})
