from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),

    path('', views.index),
    path('<int:tahun>/<int:bulan>/<int:hari>/', views.articles),
    path('<int:value>/', views.angka),
    # url(r'(?P<tahun>[0-9]{4})/(?P<bulan>[0-9]{2})/(?P<hari>[0-9]{2})/', views.tanggal),
    # url(r'(?P<page>[\w-]+)/', views.link)
    path('<str:page>/', views.link)
]
