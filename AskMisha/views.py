from django.http import HttpResponse
#from faker import Faker
from django.core.paginator import Paginator
from django.shortcuts import render
from questions.models import *


def index(request):
    context = {
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'index.html', context)


def ask(request):
    context = {
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'ask.html', context)


def login(request):
    context = {
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'login.html', context)


def registration(request):
    context = {
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'register.html', context)


def settings(request):
    context = {
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'settings.html', context)


def tag(request, tag_name):
    context = {
        'tags': Tag.objects.all()[:7],
        'tag_name': tag_name,
    }
    return render(request, 'tag.html', context)


def questions(request):
    context = {
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'questions.html', context)
