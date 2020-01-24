
from accounts.forms import CustomPasswordResetForm
from rest_auth.serializers import PasswordResetSerializer
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.forms import ResetPasswordForm
from django.conf import settings
from rest_framework import serializers
from accounts.models import Profile, ProfilePreferenzeMateria, ProfileInterrogazione
from django.contrib.auth.models import User
from django.core import serializers as djangoSerializers
import json
from django.core.serializers.json import DjangoJSONEncoder

from classi import serializers as classi_serializers
from classi import models as classi_models


class CustomPasswordResetSerializer(PasswordResetSerializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    password_reset_form_class = CustomPasswordResetForm


class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
        }


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    
    def get_profile(self, data):
        queryset = Profile.objects.filter(id=data.profile.id)
        serializer_Profile = ProfileUserDetailsSerializer(queryset, many=True)
        data = serializer_Profile.data
        return json.loads(json.dumps(list(data), cls=DjangoJSONEncoder))
    
    class Meta:
        model = User
        fields = ('email', 'username' , 'profile')
        read_only_fields = ('email',)


class ProfileUserDetailsSerializer(serializers.ModelSerializer):

    materie_preferite = serializers.SerializerMethodField()
    interrogazioni = serializers.SerializerMethodField()
    classe_info = serializers.SerializerMethodField()

    def get_materie_preferite(self, data):
        queryset = ProfilePreferenzeMateria.objects.filter(profile=data.id)
        serializer_PreferenzeMateria = ProfilePreferenzeMateriaSerializer(queryset, many=True)
        data = serializer_PreferenzeMateria.data
        return json.loads(json.dumps(list(data), cls=DjangoJSONEncoder))
        
    def get_interrogazioni(self, data):
        queryset = ProfileInterrogazione.objects.filter(profile=data.id)
        serializer_ProfileInterrogazione = ProfileInterrogazioneSerializer(queryset, many=True)
        data = serializer_ProfileInterrogazione.data
        return json.loads(json.dumps(list(data), cls=DjangoJSONEncoder))

    def get_classe_info(self, data):
        queryset = classi_models.Classe.objects.filter(pk=data.classe.id)
        serializer_Classe = classi_serializers.ClasseSerializer(queryset, many=True)
        data = serializer_Classe.data
        return json.loads(json.dumps(list(data), cls=DjangoJSONEncoder))

    class Meta:
        model = Profile
        fields = ('id','user','first_name','last_name','classe','classe_info','interrogazioni','telephone', 'avatar_image' , 'materie_preferite', 'complete_progress',)
        read_only_fields = ('user',)

class ProfilePreferenzeMateriaSerializer(serializers.ModelSerializer):
    materia_nome = serializers.ReadOnlyField(source='materia.nome')
    class Meta:
        model = ProfilePreferenzeMateria
        fields = ('id','profile','materia','materia_nome','valore',)


class ProfileInterrogazioneSerializer(serializers.ModelSerializer):

    turno_interrogazione = serializers.SerializerMethodField()

    def get_turno_interrogazione(self, data):
        queryset = classi_models.ClasseTurnoInterrogazione.objects.filter(pk=data.turnointerrogazione)
        serializer_ClasseTurnoInterrogazione = classi_serializers.ClasseTurnoInterrogazioneSerializer(queryset, many=True)
        data_x = serializer_ClasseTurnoInterrogazione.data
        return json.loads(json.dumps(list(data_x), cls=DjangoJSONEncoder))

    class Meta:
        model = ProfileInterrogazione
        fields = ('id','profile','voto','turnointerrogazione','turno_interrogazione','conferma')
