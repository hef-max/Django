from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def list(request):
    return render(request, "list.html")

def community(request):
    return render(request, "community.html")

def faq(request):
    return render(request, "faq.html")