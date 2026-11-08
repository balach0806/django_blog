from django.shortcuts import render
from django.http import HttpResponse
from .data import CATEGORIES, POSTS

def index(request):
    return HttpResponse("<h1>Моя главная страница проекта на Django-blog.</h1>")