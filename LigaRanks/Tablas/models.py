from django.db import models

# Create your models here.

class Equipo(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=3, default='---')
	escudo = models.ImageField(upload_to='logos')
	puntos = models.IntegerField(default=0)
	goles_favor = models.IntegerField(default=0)
	goles_contra = models.IntegerField(default=0)

	def __unicode__(self):
		return self.codigo

	def __lt__(self, other):
		return self.puntos < other.puntos

class Jornada(models.Model):
	numero = models.IntegerField(unique=True)

	def __unicode__(self):
		return "J" + str(self.numero)

class Partido(models.Model):
	SE_HA_JUGADO=(('S', 'Si'),('N', 'No'))
	equipo_local = models.ForeignKey(Equipo, related_name='local')
	equipo_visitante = models.ForeignKey(Equipo, related_name='visitante')
	jugado = models.CharField(max_length=1, choices=SE_HA_JUGADO, default='S')
	goles_local = models.IntegerField(default=0)
	goles_visitante = models.IntegerField(default=0)
	jornada = models.ForeignKey(Jornada)

	def __unicode__(self):
		return unicode(self.jornada) + "-" + unicode(self.equipo_local) + "-" + unicode(self.equipo_visitante)
	
	

#Activar en el panel de control desde admin.py
#python manage.py syncdb
#makemigrations y migrate.
#manage.py sql Tablas.
