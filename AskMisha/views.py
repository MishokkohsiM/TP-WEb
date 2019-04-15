from django.shortcuts import render, redirect, get_object_or_404
from questions.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        'questions': Question.objects.all()[:3],
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
    current_tag = get_object_or_404(Tag, title=tag_name)
    questions = Question.objects.new().filter(tag=current_tag)
    questions = paginate(questions, request)

    context = {
        'questions': questions,
        'tag': current_tag,
        'tags': Tag.objects.all()[:7],
        'users': User.objects.all()[:5],
    }

    return render(request, 'tag.html', context)


def question(request, questions_name):
    current_question = get_object_or_404(Question, title=questions_name)
    context = {
        'question': current_question,
        'tags': Tag.objects.all()[:7],
    }
    return render(request, 'questions.html', context)


def paginate(objects_list, request):
    paginator = Paginator(objects_list, 3)

    try:
        questions = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(1)
    return questions
