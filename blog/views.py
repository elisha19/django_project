from djproject.settings import USE_TZ
from django.shortcuts import render
from django.http import request

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
