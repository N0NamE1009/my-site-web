from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home/home.html")

def about(request):
    return render(request,"about/about.html")

def portfolio(request):
    return render(request,"portfolio/portfolio.html")

def contact(request):
    return render(request,"contact/contact.html")
