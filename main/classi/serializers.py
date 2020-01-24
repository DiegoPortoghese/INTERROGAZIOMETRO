from rest_framework import serializers
from classi import models
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers as xxx
from drf_extra_fields.fields import Base64ImageField
#From APP ACCOUNTS
from accounts import models as accounts_models
from accounts import serializers as accounts_serializers

import json


class ClasseSerializer(serializers.ModelSerializer):
    
    owner_first_name = serializers.ReadOnlyField(source='creatore.profile.first_name')
    owner_last_name = serializers.ReadOnlyField(source='creatore.profile.last_name')
    orario = serializers.SerializerMethodField()
    alunni = serializers.SerializerMethodField()
    #services_description = serializers.SerializerMethodField()
    

    def get_orario(self, data):
        # fare meglio
        # https://stackoverflow.com/questions/44313073/django-rest-serializers-based-on-multiple-querysets
        queryset = models.ClasseOraMateria.objects.filter(classe=data.id)
        serializer_OraMateria = ClasseOraMateriaSerializer(queryset, many=True)
        data = serializer_OraMateria.data
        return json.loads(json.dumps(list(data), cls=DjangoJSONEncoder))
    
    def get_alunni(self, data):
        # fare meglio
        # https://stackoverflow.com/questions/44313073/django-rest-serializers-based-on-multiple-querysets
        queryset = accounts_models.Profile.objects.filter(classe=data.id).values('id','user','first_name','last_name')
        # serializer_Profile = accounts_serializers.ProfileUserDetailsSerializer(queryset, many=True)
        # data = serializer_Profile.data
        return json.loads(json.dumps(list(queryset), cls=DjangoJSONEncoder))
    """
    def get_services_description(self, data):
        # fare meglio
        # https://stackoverflow.com/questions/44313073/django-rest-serializers-based-on-multiple-querysets
        queryset = models.RoomService.objects.filter(room=data.id).values('id','category','title')
        #return xxx.serialize('json', queryset, fields=('file'))
        return json.loads(json.dumps(list(queryset), cls=DjangoJSONEncoder))
    """

    class Meta:

        fields = (
            'id',
            'attiva',
            'creatore',
            'owner_first_name',
            'owner_last_name',
            'nome',
            'descrizione',
            'note',
            'creation_date',
            'last_modified',
            'anno',
            'sezione',
            'immagine_copertina',
            'alunni',
            'creation_progress',
            #'numero_alunni',
            'orario',
            
        )
        model = models.Classe


class ClasseImageSerializer(serializers.ModelSerializer):
    file=Base64ImageField()
    class Meta:
        model = models.ClasseImage
        fields = '__all__'


class ClasseOraMateriaSerializer(serializers.ModelSerializer):
    materia_nome = serializers.ReadOnlyField(source='materia.nome')
    class Meta:
        model = models.ClasseOraMateria
        fields = (
            'id',
            'numero_ora',
            'giorno_della_settimana',
            'get_giorno_della_settimana_display',
            'classe',
            'materia',
            'materia_nome'
        )
        
        

class ClasseTurnoInterrogazioneSerializer(serializers.ModelSerializer):
    materia_nome = serializers.ReadOnlyField(source='materia.nome')
    class Meta:
        model = models.ClasseTurnoInterrogazione
        fields = (
            'id',
            'classe',
            'numero_interrogati',
            'stato',
            'materia',
            'materia_nome',
            'data',
        )
     


class PianificazioniTurniSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    id_turno = serializers.IntegerField(required=True)
    data = serializers.DateTimeField(required=True)
    materia_turno = serializers.IntegerField(required=True)
    class Meta:
        fields = ('id', 'id_turno','data','materia_turno')

        
"""
class RoomServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomService
        fields = '__all__'
"""