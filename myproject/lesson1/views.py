import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Здесь будет много интересного контента.</p>
    """
    logger.info(f'Пользователь посетил страницу "Главная"')
    return render(request, 'home.html', {'html': html})

def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Я - разработчик этого сайта. Увлекаюсь программированием и разработкой веб-приложений.</p>
    """
    logger.info(f'Пользователь посетил страницу "О себе"')
    return render(request, 'about.html', {'html': html})

"""
def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("About us")
"""