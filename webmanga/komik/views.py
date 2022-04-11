from django.shortcuts import render

# Create your views here.

def judul(request):
	contex = {
	'title':'Amorevole Story',
	'judul': 'berlari',
	}
	return render(request, 'episode1/judul.html', contex)