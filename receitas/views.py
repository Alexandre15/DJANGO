from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# HTTP REQUEST
def home(request):
    # return HttpResponse
    # return HttpResponse('<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Grouping Tags</title><style>body {font-family: Arial, Helvetica, sans-serif;background-color: dimgray;margin: 0px;}header {background-color: white;padding: 10px;margin: 10px;}nav {background-color: rgb(105, 105, 105);padding: 3px;box-shadow: 2px 2px 4px 1px rgba(0, 0, 0, 0.452);}nav > a {text-decoration: none;color: white;font-weight: bold;margin-right: 30px;}nav > a:hover {text-decoration: underline;}main {background-color: white;padding: 10px;margin: 10px;border-radius: 10px 0px;box-shadow: 4px 4px 9px 0px rgba(0, 0, 0, 0.397);}article {background-color: lightgray;padding: 5px;}article > aside {background-color: rgb(165, 165, 165);}footer {background-color: black;color: white;text-align: center;padding: 4px;margin: 0px;box-shadow: 0px -3px 4px 1px rgba(0, 0, 0, 0.527);}footer > p {margin: 0px;}div#bola {height: 100px;width: 100px;margin: 100px;background-color: white;border-radius: 50%;}</style></head><body><header><h1>Meu site</h1><nav><a href="#">Link</a><a href="#">Link</a><a href="#">Link</a><a href="#">Link</a><a href="#">Link</a></nav></header><main><section id="assuntos"><p>Esportes Política Tecnologia</p></section><section id="noticias"><article><h2>Notícia sobre o Brasil</h2><p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci quod quo, doloribus odio inventore ab alias ad officiis eaque vitae similique fugit repudiandae, illo delectus eum rerum. Suscipit, natus eligendi!</p><aside><p>Artigo escrito por Alexandre Fagundes</p></aside></article><article></article></section></main><footer><p>Desenvolvido pelo CursoemVideo</p></footer><div id="bola"></div></body></html>')
    # return HttpResponse("<h1>HOME views</h1>")
    return render(request, 'receitas/home.html', context={'name': 'Alexandre Fagundes'}) # Variável "name" para o template HOME


def contato(request):
    # return HttpResponse
    return HttpResponse("<h1>CONTATO views</h1>")


def sobre(request):
    # return HttpResponse
    return HttpResponse("<h1>SOBRE views</h1>")