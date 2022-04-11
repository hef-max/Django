from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
	posts = Post.objects.all()

	contex = {
		'title' : "query",
		'heading' : "selamat datang",
		'category':'all',
		'Posts' : posts

	}
	return render(request, 'index.html', contex)
def berita(request):
	posts = Post.objects.filter(category="berita")

	contex = {
		'title' : "query",
		'heading' : "selamat datang",
		'category': 'Berita',
		'Posts' : posts

	}
	return render(request, 'index.html', contex)
def gosip(request):
	posts = Post.objects.filter(category="gosip")

	contex = {
		'title' : "query",
		'heading' : "selamat datang",
		'category':'gosip',
		'Posts' : posts

	}
	return render(request, 'index.html', contex)