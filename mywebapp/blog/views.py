#views blog
from django.shortcuts import render

def index(request):
    contex = {
        'judul':'home',
        'kontributor':'hefry',
        
    }
    return render(request, 'blog/index.html', contex)

def news(request):
    contex = {
        'judul' : 'berita',
        'kontributor' : 'luna'
    }
    return render(request, 'blog/index.html', contex)

def cerita(request):
    contex = {
        'judul' : 'cerita',
        'kontributor' : 'hefy'
    }
    return render(request, 'blog/index.html', contex)