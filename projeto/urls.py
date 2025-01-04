"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# HTTP REQUEST
def my_view(request):
    # return HttpResponse
    #return HttpResponse('<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Grouping Tags</title><style>body {font-family: Arial, Helvetica, sans-serif;background-color: dimgray;margin: 0px;}header {background-color: white;padding: 10px;margin: 10px;}nav {background-color: rgb(105, 105, 105);padding: 3px;box-shadow: 2px 2px 4px 1px rgba(0, 0, 0, 0.452);}nav > a {text-decoration: none;color: white;font-weight: bold;margin-right: 30px;}nav > a:hover {text-decoration: underline;}main {background-color: white;padding: 10px;margin: 10px;border-radius: 10px 0px;box-shadow: 4px 4px 9px 0px rgba(0, 0, 0, 0.397);}article {background-color: lightgray;padding: 5px;}article > aside {background-color: rgb(165, 165, 165);}footer {background-color: black;color: white;text-align: center;padding: 4px;margin: 0px;box-shadow: 0px -3px 4px 1px rgba(0, 0, 0, 0.527);}footer > p {margin: 0px;}div#bola {height: 100px;width: 100px;margin: 100px;background-color: white;border-radius: 50%;}</style></head><body><header><h1>Meu site</h1><nav><a href="#">Link</a><a href="#">Link</a><a href="#">Link</a><a href="#">Link</a><a href="#">Link</a></nav></header><main><section id="assuntos"><p>Esportes Política Tecnologia</p></section><section id="noticias"><article><h2>Notícia sobre o Brasil</h2><p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci quod quo, doloribus odio inventore ab alias ad officiis eaque vitae similique fugit repudiandae, illo delectus eum rerum. Suscipit, natus eligendi!</p><aside><p>Artigo escrito por Alexandre Fagundes</p></aside></article><article></article></section></main><footer><p>Desenvolvido pelo CursoemVideo</p></footer><div id="bola"></div></body></html>')
    return HttpResponse("<h1>HOME</h1>")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_view),
    path('sobre/', my_view),
    path('contato/', my_view),
]
