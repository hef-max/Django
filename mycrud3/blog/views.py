from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm
from .models import PostModel

# Create your views here.

def index(request):
	posts = PostModel.objects.all()
	post_form = PostForm(request.POST or None)
	
	context = {
		'post_form' : post_form,
		"page_title": "List Post",
		"posts": posts,
	}
	return render(request, 'blog/index.html', context)

def tables(request):
	posts = PostModel.objects.all()
	context = {
        "page_title": "tables",
		"posts": posts
    }
	return render(request, 'blog/tables.html', context)

def create(request):
	post_form = PostForm(request.POST or None)
	if request.method == 'POST':
		if post_form.is_valid():
			post_form.save()
			return HttpResponseRedirect('/blog/')

	context = {
		'page_title': 'Tambah Data',
		'post_form' : post_form,
	}
	return render(request, 'blog/create.html', context)


def update(request, up_id):
	update = PostModel.objects.get(id=up_id)
	data = {
		"nim": update.nim,
		"nama": update.nama,
		"jk": update.jk,
		"tanggal_lahir": update.tanggal_lahir,
		"prodi": update.prodi,
	}
	post_form = PostForm(request.POST or None, initial=data, instance=update)

	if request.method == 'POST':
		if post_form.is_valid():
			post_form.save()
			return HttpResponseRedirect('/blog/')

	context = {
		'page_title': 'Edit Data',
		"post_form": post_form,
	}
	return render(request, 'blog/update.html', context)


def delete(request, del_id):
	PostModel.objects.filter(id=del_id).delete()
	return HttpResponseRedirect('/blog/')