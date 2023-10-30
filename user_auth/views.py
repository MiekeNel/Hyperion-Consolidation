from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


def authenticate_user(request):
    """
    View function to authenticate a user.

    This view receives a POST request with a username and password, attempts to authenticate the user,
    and logs them in if authentication is successful.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the shopping index if authentication is successful,
        or to the user_auth:login view if authentication fails.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        print("Oops! Username or Password is incorrect. \n Please try again.")
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('shopping:index'))

def user_registration(request):
    """
    View function for user registration.

    This view handles user registration. If the request method is POST, it creates a new user
    with the provided username, password, and first name. If the request method is not POST,
    it renders the registration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the user_auth:login view after successful registration.
        Renders the registration form if the request method is not POST.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        user = User.objects.create_user(username=username, password=password, first_name=first_name)
        user.save()
        return HttpResponseRedirect(reverse('user_auth:login'))
    return render(request, 'authentication/registration.html')
