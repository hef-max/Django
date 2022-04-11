from django.shortcuts import render

def main(request):
	contex = {
	'title':'CULINARY HOUSE',
	'provinsi': [
		['jawabarat/', 'Jawa Barat'],
		['jawatengah/', 'Jawa Tengah'],
		['jawatimur/', 'Jawa Timur']
	],
		'email': 'Culinaryhouseindonesia@gmail.com',
		'instagram': '@culinaryhouse.id'
	}
	return render(request, 'main.html', contex)

def jawabarat(request):
	contex = {
		'title': 'CULINARY WEST JAVA',
		'logo':'Culinary House',
		'place': [
			['place/kabbandung', 'kabupaten bandung'],
			['place/kabbanbar', 'kabupaten bandung barat'],
			['place/kabbekasi', 'kabupaten bekasi'],
			['place/kabbogor', 'kabupaten bogor'],
			['place/kabciamis', 'kabupaten ciamis'],
			['place/kabcianjur', 'kabupaten cianjur'],
			['place/kabcirebon', 'kabupaten cirebon'],
			['place/kabgarut', 'kabupaten garut'],
			['place/kabindramayu', 'kabupaten indramayu'],
			['place/kabkerawang', 'kabupaten kerawang'],
			['place/kabkuningan', 'kabupaten kuningan'],
			['place/kabmajalengka', 'kabupaten majalengka'],
			['place/kabpengandaran', 'kabupaten pengandaran'],
			['place/kabpurwakarta', 'kabupaten purwakarta'],
			['place/kabsubang', 'kabupaten subang'],
			['place/kabsukabumi', 'kabupaten sukabumi'],
			['place/kabsumedang', 'kabupaten sumedang'],
			['place/kabtasikmalaya', 'kabupaten tasikmalaya'],
			['place/kotbandung', 'kota bandung'],
			['place/kotbanjar', 'kota banjar'],
			['place/kotbekasi', 'kota bekasi'],
			['place/kotbogor', 'kota bogor'],
			['place/kotcimahi', 'kota cimahi'],
			['place/kotcirebon', 'kota cirebon'],
			['place/kotdepok', 'kota depok'],
			['place/kotsukabumi', 'kota sukabumi'],
			['place/kottasikmalaya', 'kota tasikmalaya']
		]
	}
	
	return render(request, 'index.html', contex)