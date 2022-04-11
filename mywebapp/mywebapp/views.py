from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    input = {
        'kontributor' : 'hefry',
        'nav' : [
            ['/', 'home'],
            ['/blog', 'blog'],
            ['/about', 'about'],
            ['/contact', 'contact']
        ]
    }
    return render(request, 'index.html', input)

def about(request):
    return HttpResponse('<h1> ini adalah about </h1>')

def contact(request):
    return HttpResponse('<h1> ini adalah contact </h1>')
