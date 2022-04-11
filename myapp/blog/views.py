from django.shortcuts import render

# Create your views here.

def index(request):
	contex = {
		'title':'blog'
	}
	return render(request, "blog/index.html", contex)