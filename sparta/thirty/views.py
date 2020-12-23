from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sparta(request):
    return HttpResponse("Welcome to this world")
