from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='blog'),
	path('tables/', views.tables, name='tables'),
	path('create/', views.create, name='create'),
	path('delete/<int:del_id>', views.delete, name='delete'),
	path('update/<int:up_id>', views.update, name='update'),
]