from django.http import HttpResponse

def link(request, page):

	str = "<h1>{}</h1>".format(page)
	return HttpResponse(str)



def index(request):
	return HttpResponse("<h1>home</h1>")

def angka(request, **input):

	value = input['value']

	heading = "<h1>page angka</h1>"
	str = heading + "{}".format(value)

	return HttpResponse(str)

def tanggal(request, **input):

	tahun = input['tahun']
	bulan = input['bulan']
	hari = input['hari']

	heading = "<h1>page tanggal</h1>"

	str = heading + "<h2>{}/{}/{}</h2>".format(tahun, bulan, hari)

	return HttpResponse(str)


def articles(request, **input):
	tahun = input['tahun']
	bulan = input['bulan']
	hari = input['hari']

	heading = "<h1>page articles</h1>"

	str = heading + "<h2>{}/{}/{}</h2>".format(tahun, bulan, hari) 

	return HttpResponse(str)