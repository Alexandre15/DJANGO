from django.shortcuts import render
from django.http import HttpResponse
from utils.receitas.factory import make_recipe


# Create your views here.

# HTTP REQUEST
def home(request):
    # return HttpResponse("<h1>HOME views</h1>")
    return render(request, 'receitas/pages/home.html', context={'recipes': [make_recipe() for _ in range(10)]}) # Variável "name" para o template HOME

def receita(request, id):
    # return HttpResponse("<h1>HOME views</h1>")
    return render(request, 'receitas/pages/receita.html', context={'recipe': make_recipe()}) # Variável "name" para o template HOME