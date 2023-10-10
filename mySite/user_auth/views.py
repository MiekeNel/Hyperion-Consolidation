from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
#def user_login(request):
#   return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        print("Oops! Username or Password is incorrect. \n Please try again.")
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('shopping:index'))

    
#def show_user(request):
#    print(request.user.username)
#    return render(request, 'authentication/user.html', {
#        "username": request.user.username,
#        "password": request.user.password
#    })

def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        user = User.objects.create_user(username=username, password=password, first_name=first_name)
        user.save()
        return HttpResponseRedirect(reverse('user_auth:login'))
    return render(request, 'authentication/registration.html')