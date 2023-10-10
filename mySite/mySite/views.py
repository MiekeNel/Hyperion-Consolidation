from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # View logic for the home page
    return HttpResponse("Welcome to mySite!")

def about(request):
    # View logic for the about page
    return HttpResponse("This is the about page.")
