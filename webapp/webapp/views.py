from django.shortcuts import render


def index(request):
	contex = {
		'judul':'kelastertutup',
		'subjudul':'selamat datang',
		'banner':'img/banner_home.png'
	}
	return render(request, 'index.html', contex)