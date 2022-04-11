from django.urls import path
from . import views


urlpatterns = [
	path('kabbandung/', views.kabbandung),
	path('kabbanbar/', views.kabbanbar),
	path('kabbekasi/', views.kabbekasi),
	path('kabbogor/', views.kabbogor),
	path('kabciamis/', views.kabciamis),
	path('kabcianjur/', views.kabcianjur),
	path('kabcirebon/', views.kabcirebon),
	path('kabgarut/', views.kabgarut),
	path('kabindramayu/', views.kabindramayu),
	path('kabkerawang/', views.kabkerawang),
	path('kabkuningan/', views.kabkuningan),
	path('kabmajalengka/', views.kabmajalengka),
	path('kabpengandaran/', views.kabpengandaran),
	path('kabpurwakarta/', views.kabpurwakarta),
	path('kabsubang/', views.kabsubang),
	path('kabsukabumi/', views.kabsukabumi),
	path('kabsumedang/', views.kabsumedang),
	path('kabtasikmalaya/', views.kabtasikmalaya),
	path('kotbandung/', views.kotbandung),
	path('kotbanjar/', views.kotbanjar),
	path('kotbekasi/', views.kotbekasi),
	path('kotbogor/', views.kotbogor),
	path('kotcimahi/', views.kotcimahi),
	path('kotcirebon/', views.kotcirebon),
	path('kotdepok/', views.kotdepok),
	path('kotsukabumi/', views.kotsukabumi),
	path('kottasikmalaya/', views.kottasikmalaya),
]