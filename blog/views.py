from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import request

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home page!</h1>")

def about(request):
    return HttpResponse("<h1>Home page!</h1>")