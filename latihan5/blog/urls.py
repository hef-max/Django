from django.urls import path
from . import views

urlpatterns = [
	path('blog/', views.index),
	path('berita/', views.berita),
	path('gosip/', views.gosip),
]