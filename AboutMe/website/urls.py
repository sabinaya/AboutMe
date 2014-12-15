from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='home'),
	    url(r'^about/', views.about, name='about'),
	    url(r'^index/', views.index, name='index'),
)
