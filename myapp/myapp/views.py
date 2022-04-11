from django.shortcuts import render


def index(request):
	contex = {
		'title':'kelastertutup',
		'heading':'selamat datang',

	}
	return render(request, 'index.html', contex)