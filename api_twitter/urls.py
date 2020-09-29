from django.conf.urls import url 
from api_twitter import views 

urlpatterns = [ 
    url(r'^countries/$', views.countries_list),
]