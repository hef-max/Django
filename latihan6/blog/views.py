from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post

def index(request):

	return HttpResponse("home")

def categoryPost(request, input):
	posts = Post.objects.filter(category=input)

	return HttpResponse("categoryPost")

def singlePost(request, slugInput):
	posts = Post.objects.get(slug=slugInput)

	judul = "<h1>{}</h1>".format(posts.judul)
	body = "<h2>{}</h2>".format(posts.body)
	category = "<p>{}</p>".format(posts.category)

	return HttpResponse(judul + body +  category)