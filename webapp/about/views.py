# views about
from django.shortcuts import render


def index(request):
	contex = {
		'judul':'kelastertutup',
		'subjudul':'tentang',
		'banner':'about/img/banner_about.png',
		'app_css':'about/css/style.css',
	}
	return render(request, 'index.html', contex)