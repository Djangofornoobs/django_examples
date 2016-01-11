from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.views.generic.list import ListView
from django import forms
from django.conf import settings
from datetime import datetime
import os
# Create your models here.

# Un destino es un lugar al que se puede viajar, pero sin incluir los datos respecto al viaje, como precio, etc...
class Destino(models.Model):
	lugar = models.CharField(max_length=100)
	descripcion = models.TextField()
	distancia = models.IntegerField()
	
	def __unicode__(self):
        	return self.lugar

class Viaje(models.Model):
	destino = models.ForeignKey(Destino, related_name='destino')
	dias = models.IntegerField()
	coste = models.FloatField()
	
	def __unicode__(self):
        	return self.destino

class Ruta(models.Model):
	viajes = models.ManyToManyField(Viaje, related_name='viajes', blank=True, null=True)
	totalDias = models.IntegerField(blank=True, null=True)
	totalCoste = models.FloatField(blank=True, null=True)

	def save(self, *args, **kwargs):
    	    if self.pk is None:
      		  super(Ruta, self).save(*args, **kwargs)
	    for a in self.viajes.all():
		self.totalDias += a.dias
		self.totalCoste += a.coste
	    super(Ruta, self).save(*args, **kwargs)


class ViajeForm(ModelForm):
	class Meta:
		model = Viaje
		fields = ['destino', 'dias', 'coste']	

	def __init__(self, *args, **kwargs):
		super(ViajeForm, self).__init__(*args, **kwargs)
		self.fields['destino'].label = "Destino del viaje"
		self.fields['dias'].label = "Dias del viaje"
		self.fields['coste'].label = "Coste del viaje"


	def save(self, commit=True):
		viajeform = super(ViajeForm, self).save(commit=False)
		if commit:
			viajeform.save()
		return viajeform

class RutaForm(ModelForm):
	class Meta:
		model = Ruta
		fields = ['viajes']	

	def __init__(self, *args, **kwargs):
		super(RutaForm, self).__init__(*args, **kwargs)
		self.fields['viajes'].label = "Viajes de la ruta"


	def save(self, commit=True):
		rutaform = super(RutaForm, self).save(commit=False)
		if commit:
			rutaform.save()
		return rutaform


class DestinoForm(ModelForm):
	class Meta:
		model = Destino
		fields = ['lugar', 'descripcion', 'distancia']	

	def __init__(self, *args, **kwargs):
		super(DestinoForm, self).__init__(*args, **kwargs)
		self.fields['lugar'].label = "Lugar del destino"
		self.fields['descripcion'].label = "Descripcion del destino"
		self.fields['distancia'].label = "Distancia del destino"


	def save(self, commit=True):
		destinoform = super(DestinoForm, self).save(commit=False)
		if commit:
			destinoform.save()
		return destinoform

