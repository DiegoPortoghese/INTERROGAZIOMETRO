from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name= models.CharField(max_length=100, blank=True, null=True)
    last_name= models.CharField(max_length=100, blank=True, null=True)

    telephone = models.CharField(max_length=30, blank=True, null=True)
    cap = models.CharField(max_length=10, blank=True, null=True)
    province = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    newsletter_consent = models.BooleanField(default=False)
    privacy_consent = models.BooleanField(default=False)

    avatar_image = models.ImageField(blank=False, null=True, upload_to="rooms/img/%Y/%m/%d")
    # materie_preferite = models.ManyToManyField('ProfilePreferenzeMateria', blank=True, verbose_name=_(u"Materie preferite"))

    classe = models.ForeignKey('classi.Classe', related_name='ProfileClasse', verbose_name=_(u"Classe"), on_delete=models.CASCADE, default=1)
    
    complete_progress = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class ProfilePreferenzeMateria(models.Model):
    profile = models.ForeignKey('Profile', related_name='ProfilePreferenzeMateria', verbose_name=_(u"Profile"), on_delete=models.CASCADE, default=1)
    materia = models.ForeignKey('classi.ClasseMateria', related_name='PreferenzaMateria', verbose_name=_(u"Materia"), on_delete=models.CASCADE, default=1)
    valore = models.IntegerField(default=0)
    
    def __str__(self):
        return self.valore


class ProfileInterrogazione(models.Model):
    profile = models.ForeignKey('Profile', related_name='ProfileInterrogazione', verbose_name=_(u"Profile"), on_delete=models.CASCADE, default=1)
    turnointerrogazione = models.ForeignKey('classi.ClasseTurnoInterrogazione', related_name='ProfileClasseTurnoInterrogazione', verbose_name=_(u"ProfileClasseTurnoInterrogazione"), on_delete=models.CASCADE, default=1)
    voto = models.DecimalField(max_digits=10, decimal_places=4,default=0)
    conferma = models.IntegerField(default=0)
    descrizione = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.descrizione
