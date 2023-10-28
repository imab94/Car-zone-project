from django.shortcuts import render
from django.http import HttpResponse
from .models import Team

# Create your views here.

def index(request):
    teams = Team.objects.all()
    return render(request, 'pages/home.html',{"teams": teams})

def about(request):
    teams = Team.objects.all()
    return render(request, 'pages/about.html',{"teams": teams})

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')