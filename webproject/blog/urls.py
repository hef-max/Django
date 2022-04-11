from django.urls import path
from .views import *

urlpatterns = [
	path('post1', Kabbandung.post1),
	path('post2', Kabbandung.post2),
]