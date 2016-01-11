from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # url(r'^AgenciaViajes/', include('AgenciaViajes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addDestino/$', 'viajes.views.nuevoDestino'),
    url(r'^listadestinos/$', 'viajes.views.listaDestinos', name='destinoList'),
    url(r'^listadestinos/(?P<destino_id>\d+)$', 'viajes.views.destinoDetail', name = 'destino'),
    url(r'^addViaje/$', 'viajes.views.nuevoViaje'),
    url(r'^listaviaje/$', 'viajes.views.listaViaje', name='viajeList'),
    url(r'^listaviaje/(?P<viaje_id>\d+)$', 'viajes.views.viajeDetail', name = 'viaje'),
    url(r'^editarviaje/(?P<viaje_id>\d+)$', 'viajes.views.editarViaje', name='editarViaje'),
    url(r'^addRuta/$', 'viajes.views.nuevaRuta'),
    url(r'^listaruta/$', 'viajes.views.listaRuta', name='rutaList'),
    url(r'^login/$', 'viajes.views.ingresar'),
    url(r'^logout/$', 'viajes.views.cerrar'),
)
