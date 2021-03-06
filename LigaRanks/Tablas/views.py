#-*- encoding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
#NUEVAS
from django.core.paginator import Paginator, InvalidPage, EmptyPage #Por si le pongo páginas
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from Tablas.models import *
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from forms import SignUpForm

def index(request):
	equipos = Equipo.objects.all().order_by("-puntos")
	partidos = Partido.objects.all()
	jornadas = Jornada.objects.all()
	for equipo in equipos:
		for partido in partidos:
			if partido.equipo_local==equipo and partido.jugado=='S':
				equipo.goles_favor += partido.goles_local
				equipo.goles_contra += partido.goles_visitante
				if partido.goles_local > partido.goles_visitante:
					equipo.puntos += 3
				if partido.goles_visitante == partido.goles_local:
					equipo.puntos += 1
			if partido.equipo_visitante==equipo and partido.jugado=='S':
				equipo.goles_favor += partido.goles_visitante
				equipo.goles_contra += partido.goles_local
				if partido.goles_local < partido.goles_visitante:
					equipo.puntos += 3
				if partido.goles_visitante == partido.goles_local:
					equipo.puntos += 1
		l_equipos = list(equipos)
		l_equipos.sort(key=lambda x: (x.puntos, x.goles_favor-x.goles_contra, x.goles_favor), reverse=True)
		
	"""paginator = Paginator(equipo,3)

	try:

		pagina = int(request.GET.get("page", '1'))
	except ValueError:
		pagina = 1

	try:
		equipo = paginator.page(pagina)
	except (InvalidPage, EmptyPage):
		equipo = paginator.page(paginator.num_pages)"""

	return render_to_response("clasificacion.html",dict(equipos = l_equipos, partidos = partidos, jornadas = jornadas, user = request.user))

def detail(request, code):
	equipos = Equipo.objects.all().order_by("-puntos")
	partidos = Partido.objects.all()
	jornadas = Jornada.objects.all()
	for equipo in equipos:
		for partido in partidos:
			if partido.equipo_local==equipo and partido.jugado=='S':
				equipo.goles_favor += partido.goles_local
				equipo.goles_contra += partido.goles_visitante
				if partido.goles_local > partido.goles_visitante:
					equipo.puntos += 3
				if partido.goles_visitante == partido.goles_local:
					equipo.puntos += 1
			if partido.equipo_visitante==equipo and partido.jugado=='S':
				equipo.goles_favor += partido.goles_visitante
				equipo.goles_contra += partido.goles_local
				if partido.goles_local < partido.goles_visitante:
					equipo.puntos += 3
				if partido.goles_visitante == partido.goles_local:
					equipo.puntos += 1
		l_equipos = list(equipos)
		l_equipos.sort(key=lambda x: (x.puntos, x.goles_favor-x.goles_contra, x.goles_favor), reverse=True)
	return render_to_response("detalles.html",dict(code = code, equipos = l_equipos, partidos = partidos, jornadas = jornadas, user = request.user))

def calendar(request):
	equipos = Equipo.objects.all().order_by("-puntos")
	partidos = Partido.objects.all()
	jornadas = Jornada.objects.all()
	
	return render_to_response("calendario.html", dict(equipos = equipos, partidos = partidos, jornadas = jornadas, user = request.user))	

def contact(request):
	return render_to_response("contacto.html", dict(user = request.user))

def register(request):
	if request.method == 'POST':  # If the form has been submitted...
		form = SignUpForm(request.POST)  # A form bound to the POST data
		if form.is_valid():  # All validation rules pass 
		# Process the data in form.cleaned_data
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			email = form.cleaned_data["email"]
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			# At this point, user is a User object that has already been saved
			# to the database. You can continue to change its attributes
			# if you want to change other fields.
			user = User.objects.create_user(username, email, password)
			user.first_name = first_name
			user.last_name = last_name
 
			# Save new user attributes
			user.save()
			return HttpResponseRedirect(reverse('login'))  # Redirect after POST
	else:
		form = SignUpForm()
 
	data = {
		'form': form,
		'user': request.user,
	}
	return render_to_response('register.html', data, context_instance=RequestContext(request))

@login_required()
def home(request):
	return render_to_response('home.html', {'user': request.user}, context_instance=RequestContext(request))

# Create your views here.
