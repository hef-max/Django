from django.shortcuts import render

def index(request):
	contex = {
	'title': 'Amorevole Story',
	'logo':'',
	}
	return render(request, 'index.html', contex)