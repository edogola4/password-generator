from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def passgen(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    password = ""
    for x in range(15):
        password += random.choice(char)
    return render(request, 'password.html', {'password': password})
