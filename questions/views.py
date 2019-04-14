from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def ask(request):
    return render(request, 'ask.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'register.html')


def base(request):
    return render(request, 'base.html')
