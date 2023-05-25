from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def crud(request):
    return render(request, "crud.html")

def impressum(request):
    return render(request, "impressum.html")