from django.shortcuts import render, redirect, get_object_or_404
from questions.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime


def index(request):
    questions = Question.objects.order_by('-created')
    page, paginator = paginate(questions, request)
    context = {
        'users': User.objects.all()[:7],
        'questions': Question.objects.all(),
        'tags': Tag.objects.all()[:7],
        'paginate': paginator.get_page(page),
    }
    return render(request, 'index.html', context)


def ask(request):
    context = {
        'users': User.objects.all()[:5],
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'ask.html', context)


def login(request):
    context = {
        'users': User.objects.all()[:5],
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'login.html', context)


def registration(request):
    context = {
        'users': User.objects.all()[:5],
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'register.html', context)


def settings(request):
    context = {
        'users': User.objects.all()[:5],
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'settings.html', context)


def tag(request, tag_name):
    current_tag = get_object_or_404(Tag, title=tag_name)
    questions = Question.objects.new().filter(tag=current_tag)
    page, paginator = paginate(questions, request)

    context = {
        'questions': questions,
        'tag': current_tag,
        'tags': Tag.objects.all()[:7],
        'users': User.objects.all()[:5],
        'paginate': paginator.get_page(page),
    }

    return render(request, 'tag.html', context)


def question(request, questions_name):
    current_question = get_object_or_404(Question, title=questions_name)
    answer = Answer.objects.filter(question=current_question)
    context = {
        'answers': answer,
        'users': User.objects.all()[:5],
        'question': current_question,
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'questions.html', context)


def paginate(objects_list, request):
    paginator = Paginator(objects_list, 3)
    page = request.GET.get('page')
    return page, paginator
