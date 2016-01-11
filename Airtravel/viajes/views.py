from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from viajes.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from django.db import models

# Create your views here.

def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method=='POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if not user is None:
				if user.is_active:
					login(request, user)
				else:
					return render_to_response('usuarios/noactivo.html', context_instance=RequestContext(request))
			else:
					return render_to_response('usuarios/noexiste.html', context_instance=RequestContext(request))

	else:
		form= AuthenticationForm()
	return render_to_response('login.html', {'form':form}, context_instance=RequestContext(request))

def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')

#ANADIR DESTINO
def nuevoDestino(request):
	if request.method=='POST':
		form = DestinoForm(request.POST)

		if form.is_valid():
								
			form.save()

		return HttpResponseRedirect('/listadestinos')
	else:
		form = DestinoForm()

	return render_to_response('nuevoDestino.html', {'form':form}, context_instance=RequestContext(request))

def nuevaRuta(request):
	if request.method=='POST':
		form = RutaForm(request.POST)

		if form.is_valid():				
			form.save()
			

		return HttpResponseRedirect('/listadestinos')
	else:
		form = RutaForm()

	return render_to_response('nuevaRuta.html', {'form':form}, context_instance=RequestContext(request))


#LISTA DE DESTINOS
def listaDestinos(request):
	list = Destino.objects.all()
	context = {'destinoList': list}
	return render(request, 'destinoList.html', context)

def listaRuta(request):
	list = Ruta.objects.all()
	context = {'rutaList': list}
	return render(request, 'rutaList.html', context)

#DETALLES DEL DESTINO
def destinoDetail(request, destino_id):
	destino = Destino.objects.get(pk=destino_id)
	context = {'Destino': destino}
	return render(request, 'destinoDetail.html', context)


#ANADIR VIAJE
def nuevoViaje(request):
	if request.method=='POST':
		form = ViajeForm(request.POST)

		if form.is_valid():
								
			form.save()

		return HttpResponseRedirect('/listaviaje')
	else:
		form = ViajeForm()

	return render_to_response('nuevoViaje.html', {'form':form}, context_instance=RequestContext(request))

#LISTA DE VIAJES
def listaViaje(request):
	list = Viaje.objects.all()
	context = {'viajeList': list}
	return render(request, 'viajeList.html', context)

#DETALLES DEL VIAJE
def viajeDetail(request, viaje_id):
	viaje = Viaje.objects.get(pk=viaje_id)
	context = {'Viaje': viaje}
	return render(request, 'viajeDetail.html', context)

#EDITAR VIAJE
def editarViaje(request, viaje_id):
	viaje = Viaje.objects.get(pk=viaje_id)
	if request.method=='POST':
		form = ViajeForm(request.POST, instance = viaje)
		if form.is_valid():				
			form.save()
		return HttpResponseRedirect('/listaviaje/'+str(viaje.id))
	else:
		form = ViajeForm(instance = viaje)

	return render_to_response('editarViaje.html', {'form':form}, context_instance=RequestContext(request))


