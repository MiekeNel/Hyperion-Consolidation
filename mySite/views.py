from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    View function for the home page.

    This view renders a simple welcome message when the user visits the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A HTTP response with a welcome message.
    """
    return HttpResponse("Welcome to mySite!")


def about(request):
    """
    View function for the about page.

    This view renders information about the site or application when the user visits the about page.
    
    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A HTTP response with information about the site.
    """
    return HttpResponse("This is the about page.")
