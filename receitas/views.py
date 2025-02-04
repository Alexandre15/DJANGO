from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# HTTP REQUEST
def home(request):
    # return HttpResponse("<h1>HOME views</h1>")
    return render(request, 'receitas/pages/home.html', context={'name': 'Alexandre Fagundes'}) # Variável "name" para o template HOME

def receita(request, id):
    # return HttpResponse("<h1>HOME views</h1>")
    return render(request, 'receitas/pages/receita.html', context={'name': 'Alexandre Fagundes'}) # Variável "name" para o template HOME