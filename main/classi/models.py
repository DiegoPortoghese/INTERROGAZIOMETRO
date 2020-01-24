from django.db import models
from django.utils.translation import ugettext_lazy as _


CLASSE_ANNO = (
    (0, _('Nessuno')),
    (1, _('Primo')),
    (2, _('Secondo')),
    (3, _('Terzo')),
    (4, _('Quarto')),
    (5, _('Quinto')),
)

GIORNI_SETTIMANA = (
    (0, _('NoneNone')),
    (1, _('Lunedì')),
    (2, _('Martedì')),
    (3, _('Mercoledì')),
    (4, _('Giovedì')),
    (5, _('Venerdì')),
    (6, _('Sabato')),
    (7, _('Domenica')),
)

class Classe(models.Model):
    creatore = models.ForeignKey('auth.User', related_name='classi', on_delete=models.CASCADE, default=1)
    immagine_copertina = models.ImageField(blank=False, null=True, upload_to="rooms/img/%Y/%m/%d")
    nome = models.CharField(max_length=200,default='')
    descrizione = models.TextField(default='')
    note = models.TextField(default='')
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    anno = models.IntegerField(default=0, verbose_name=_(u"Anno della classe"))
    sezione = models.CharField(max_length=10,default='')
    # materie = models.ManyToManyField('ClasseMateria', blank=True, verbose_name=_(u"Materie della classe"))
    # alunni = models.ManyToManyField('auth.User', blank=True, verbose_name=_(u"Alunni della classe"))
    creation_progress = models.IntegerField(default=0)
    # numero_alunni = models.IntegerField(default=0)
    # ore_materie = models.ManyToManyField('ClasseOraMateria', blank=True, verbose_name=_(u"Alunni della classe"))
    attiva = models.BooleanField(verbose_name=_(u"Attivo"),default=True)

    def __str__(self):
        return self.nome

class ClasseMateria(models.Model):
    nome = models.CharField(max_length=200)
    description = models.TextField(default='')
    def __str__(self):
        return self.nome

class ClasseOraMateria(models.Model):
    classe = models.ForeignKey('Classe', related_name='ora_classe', on_delete=models.CASCADE, default=1)
    materia = models.ForeignKey('ClasseMateria', related_name='ora_materia', verbose_name=_(u"Materie della interrogazione"), on_delete=models.CASCADE, default=15)
    numero_ora = models.IntegerField(default=0)
    giorno_della_settimana = models.IntegerField(default=0, choices=GIORNI_SETTIMANA, verbose_name=_(u"Giorno della settimana")) # GIORNI_SETTIMANA
    
    def __str__(self):
        return self.numero_ora, self.giorno_della_settimana
    
class ClasseInterrogazione(models.Model):
    alunno_interrogato = models.ForeignKey('auth.User', related_name='ClasseInterrogazione', on_delete=models.CASCADE, default=1)
    materia = models.ManyToManyField('ClasseMateria', blank=True, verbose_name=_(u"Materia della classe"))
    voto_string = models.CharField(max_length=200)
    voto = models.DecimalField(max_digits=10, decimal_places=4,default=0)
    descrizione = models.TextField(default='')
    data_interrogazione = models.DateTimeField(default=None)
    confermato = models.BooleanField(verbose_name=_(u"Attivo"),default=False)

    def __str__(self):
        return self.title

class ClasseTurnoInterrogazione(models.Model):
    classe = models.ForeignKey('Classe', related_name='turno_interrogazione_classe', on_delete=models.CASCADE, default=1)
    materia = models.ForeignKey('ClasseMateria', related_name='turno',on_delete=models.CASCADE,verbose_name=_(u"Materie turno interrogazione"))
    data = models.DateTimeField(default=None)
    numero_interrogati = models.IntegerField(default=0)
    stato = models.IntegerField(default=0)
    
    def __int__(self):
        return self.pk

class ClasseImage(models.Model):
    file = models.ImageField(blank=False, null=False, upload_to="rooms/img/%Y/%m/%d")
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    classe = models.ForeignKey('Classe', related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name