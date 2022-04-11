from django.shortcuts import render

# Create your views here.

from .models import Post


def index(request):
	# query
	post = Post.objects.all()
	contex = {
		'title':'blog',
		'heading':'ini blog',
		'Post': post,
	}
	return render(request, 'blog/index.html', contex)