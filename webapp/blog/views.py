# views blog
from django.shortcuts import render

# Create your views here.

def index(request):
	contex = {
		'judul':'kelastertutup',
		'subjudul':'selamat datang di blog',
		'banner':'blog/img/banner_blog.png',
		'app_css':'blog/css/style.css',
	}
	return render(request, 'index.html', contex)