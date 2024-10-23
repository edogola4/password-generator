from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World</h1><br>,<h2>my first Django project!!</h2>")

def passgen(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    password = ""
    for x in range(15):
        password += random.choice(char)
    pas = {'password': password}
    
    return JsonResponse(pas)
