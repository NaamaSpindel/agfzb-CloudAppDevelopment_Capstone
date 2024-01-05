from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)

def contact(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/contact.html', context)

def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'djangoapp/login.html')
    else:
        return render(request, 'djangoapp/login.html')

def logout_request(request):
    if request.user.is_authenticated:
        print("Log out the user `{}`".format(request.user.username))
        logout(request)
    return redirect('djangoapp:index')  # Use the namespace instead of the URL

def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']  # Corrected the form field name
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_exist = User.objects.filter(username=username).exists()
        
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect('djangoapp:index')  # Use the namespace instead of the URL
        else:
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'djangoapp/registration.html', context)
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)
