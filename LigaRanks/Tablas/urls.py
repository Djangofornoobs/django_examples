from django.conf.urls import include, url, patterns
from django.contrib.auth.views import login, logout

from Tablas import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^calendario/', views.calendar, name='calendar'),
	url(r'^contacto/', views.contact, name='contact'),
	url(r'^registro/', views.register, name='register'),
	url(r'^login/', login, {'template_name': 'login.html', }, name="login"),
	url(r'^home/', views.home, name='home'),
	url(r'^logout/', logout, {'template_name': 'logout.html', }, name="logout"),
	url(r'^equipo/(?P<code>[A-Z]{3})/', views.detail),
)
