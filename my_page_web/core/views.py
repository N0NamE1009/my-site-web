from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h1>Pagina web personal</h1><h2>Portada</h2>")

def about(request):
    return HttpResponse("<h1>Pagina web personal</h1><h2>Acerca de</h2>")

def portfolio(request):
    return HttpResponse("<h1>Pagina web personal</h1><h2>Acerca de</h2>")

def contact(request):
    return HttpResponse("<h1>Pagina web personal</h1><h2>Acerca de</h2>")
