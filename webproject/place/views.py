from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def kabbandung(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Bandung',
		'banner': 'place/img/kab-bandung.jpeg',
		'logo':'Culinary House',

		#makanan 
		'img1':'place/img/makanan/kue.jpg',
		'nama':'kue',
		'link1':'/blog/post1',

		'img2':'place/img/makanan/nasipeda.jpg',
		'nama2':'nasipeda',
		'link2': '/blog/post2',

		'img3':'place/img/makanan/semdem.jpg',
		'nama3':'ini blog',
		'link3':''
	}
	return render(request, 'place/index.html', contex)

def kabbanbar(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Bandung Barat',
		'banner': 'place/img/kabband-barat.jpg',
		'logo':'Culinary House',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabbekasi(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Bekasi',
		'logo':'Culinary House',
		'banner': 'place/img/kab-bekasi.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabbogor(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Bogor',
		'logo':'Culinary House',
		'banner': 'place/img/kab-bogor.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabciamis(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Ciamis',
		'logo':'Culinary House',
		'banner': 'place/img/kab-ciamis.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabcianjur(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Cianjur',
		'logo':'Culinary House',
		'banner': 'place/img/kab-cianjur.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabcirebon(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Cirebon',
		'logo':'Culinary House',
		'banner': 'place/img/kab-cirebon.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabgarut(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Garut',
		'logo':'Culinary House',
		'banner': 'place/img/kab-garut.jpeg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabindramayu(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Indramayu',
		'logo':'Culinary House',
		'banner': 'place/img/kab-indramayu.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabkerawang(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Kerawang',
		'logo':'Culinary House',
		'banner': 'place/img/kab-kerawang.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabkuningan(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Kuningan',
		'logo':'Culinary House',
		'banner': 'place/img/kab-kuningan.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabmajalengka(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Majalengka',
		'logo':'Culinary House',
		'banner': 'place/img/kab-majalengka.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabpengandaran(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Pengandaran',
		'logo':'Culinary House',
		'banner': 'place/img/kab-pengandaran.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabpurwakarta(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Purwakarta',
		'logo':'Culinary House',
		'banner': 'place/img/kab-purwakarta.jpeg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabsubang(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Subang',
		'logo':'Culinary House',
		'banner': 'place/img/kab-subang.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabsukabumi(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Sukabumi',
		'logo':'Culinary House',
		'banner': 'place/img/kab-sukabumi.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabsumedang(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Sumedang',
		'logo':'Culinary House',
		'banner': 'place/img/kab-sumedang.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kabtasikmalaya(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kabupaten Tasikmalaya',
		'logo':'Culinary House',
		'banner': 'place/img/kab-tasikmalaya.jpeg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kotbandung(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kota Bandung',
		'logo':'Culinary House',
		'banner': 'place/img/kota-bandung.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kotbanjar(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kota Banjar',
		'logo':'Culinary House',
		'banner': 'place/img/kota-banjar.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kotbekasi(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kota Bekasi',
		'logo':'Culinary House',
		'banner': 'place/img/kota-bekasi.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kotbogor(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kota Bogor',
		'logo':'Culinary House',
		'banner': 'place/img/kota-bogor.jpeg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kotcimahi(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kota Cimahi',
		'logo':'Culinary House',
		'banner': 'place/img/kota-cimahi.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kotcirebon(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kota Cirebon',
		'logo':'Culinary House',
		'banner': 'place/img/kota-cirebon.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kotdepok(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kota Depok',
		'logo':'Culinary House',
		'banner': 'place/img/kota-depok.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kotsukabumi(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kota Sukabumi',
		'logo':'Culinary House',
		'banner': 'place/img/kota-sukabumi.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)

def kottasikmalaya(request):
	contex = {
		'title': 'CULINARY HOUSE',
		'heading': 'Kota Tasikmalaya',
		'logo':'Culinary House',
		'banner': 'place/img/kota-tasikmalaya.jpg',
		'img1':'',
		'img2':'',
		'img3':'',
	}
	return render(request, 'place/index.html', contex)
