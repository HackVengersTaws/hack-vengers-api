from django.conf.urls import url 
from api_twitter import views 

urlpatterns = [ 
    url(r'^countries/$', views.countries_list),
    url(r'^filtros/$', views.filtros),
    url(r'^tweet/$', views.tweet),
    url(r'^id/$', views.id_detail)
]

