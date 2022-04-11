from django.shortcuts import render
from .models import Posts

# Create your views here.

class Kabbandung:

	def post1(request):
		post = Posts.objects.all()
		contex = {
		'title':'CULINARY HOUSE',
		'logo':'Culinary House',
		'img': 'blog/img/kue.jpg',
		'Posts': post,
		'judul' : 'kue'	
		}
		return render(request, 'blog/index.html', contex)

	def post2(request):
		post = Posts.objects.all()
		contex = {
		'title':'CULINARY HOUSE',
		'logo':'Culinary House',
		'img': 'blog/img/nasipeda.jpg',
		'Posts': post,
		'judul':'nasipeda'
		}	
		return render(request, 'blog/index.html', contex)
	
	def post3(request):
		contex = {
		'judul':'',

		}
		return render(request, 'blog/index.html', contex)
	
	def post4(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex)
	
	def post5(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex)

class kabbandbar:

	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex)

class bekasi:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class bogor:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	


class ciamis:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class cianjur:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex)

class cirebon:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class garut:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex)

class indramayu:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class kerawang:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class kuningan:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class majalengka: 
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex)	

class pengandaran:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex)

class purwakarta:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class subang:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class sukabumi:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex)

class sumedang:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class tasik:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class kotbandung:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 

class kotbanjar:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class kotbekasi:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class kotbogor:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class kotcimahi:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex)

class kotcirebon:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class kotdepok:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	

class kotsukabumi:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex)

class kottasik:
	def post(request):
		contex = {

		}
		return render(request, 'blog/index.html', contex) 	
