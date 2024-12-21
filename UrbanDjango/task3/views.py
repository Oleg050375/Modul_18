from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def platform(request):  # функция обработки запроса на основную страницу
    return render(request, 'platform.html')

def games(request):  # функция обработки запроса на страницу магазина
    return render(request, 'games.html')

def cart(request):  # функция обработки запроса на страницу корзины
    return render(request, 'cart.html')
