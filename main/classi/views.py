from django.shortcuts import render
from rest_framework import generics, viewsets, status, exceptions, filters
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from classi import models
from accounts import models as models_accounts
from accounts import serializers as serializers_accounts
from rest_framework.renderers import JSONRenderer
from django.db.models import Q
from django.http import JsonResponse
from . import permissions
from . import serializers


class DetailClasseView(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Classe.objects.all()
    serializer_class = serializers.ClasseSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]

    def perform_update(self, serializer):
        old_progress = serializer.instance.creation_progress
        instance = serializer.save()
        new_progress = instance.creation_progress
        if old_progress >= new_progress:
            serializer.save(creation_progress=old_progress)

class ListClasseView(generics.ListCreateAPIView):
    queryset = models.Classe.objects.all().order_by('id')[0:8]
    serializer_class = serializers.ClasseSerializer
    def get_queryset(self):
        return models.Classe.objects.filter(attiva=True).order_by('id')[0:8]
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    parser_classes = (MultiPartParser,)
    
    def perform_create(self, serializer):
        serializer.save(creatore=self.request.user)

class UserListClasseView(generics.ListCreateAPIView):
    queryset = models.Classe.objects.all().order_by('-id')
    serializer_class = serializers.ClasseSerializer
    def get_queryset(self):
        return models.Classe.objects.filter(creatore=self.request.user,attiva=True).order_by('-id')
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    parser_classes = (MultiPartParser,)
    
    def perform_create(self, serializer):
        serializer.save(creatore=self.request.user)

class SearchListClasseView(generics.ListAPIView):
    queryset = models.Classe.objects.all()
    serializer_class = serializers.ClasseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descrizione']
    def get_queryset(self):
        return models.Classe.objects.filter(attiva=True).order_by('-id')
    parser_classes = (MultiPartParser,)

class ClasseImageView(generics.CreateAPIView):
    parser_classes = (MultiPartParser,)
    
    serializer_class = serializers.ClasseImageSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    
    def perform_create(self, serializer):
        if serializer.validated_data['classe'].creatore != self.request.user: # Se non è il proprietario della room , non ha i permessi
            raise exceptions.PermissionDenied(
                detail='Non hai i permessi su questa classe')
        if serializer.is_valid():
            serializer.save()


class DetailClasseImageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ClasseImage.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = serializers.ClasseImageSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    def perform_delete(self, serializer):
        if serializer.validated_data['classe'].creatore != self.request.user: # Se non è il proprietario della room , non ha i permessi
            raise exceptions.PermissionDenied(
                detail='Non hai i permessi su questa classe')
        serializer.save()



class ClasseOraMateriaView(generics.CreateAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = serializers.ClasseOraMateriaSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    
    def perform_create(self, serializer):
        if serializer.validated_data['classe'].creatore != self.request.user: # Se non è il proprietario della room , non ha i permessi
            raise exceptions.PermissionDenied(
                detail='Non hai i permessi su questa classe')
        if serializer.is_valid():
            serializer.save()


class DetailClasseOraMateriaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ClasseOraMateria.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = serializers.ClasseOraMateriaSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    def perform_delete(self, serializer):
        if serializer.validated_data['classe'].creatore != self.request.user: # Se non è il proprietario della room , non ha i permessi
            raise exceptions.PermissionDenied(
                detail='Non hai i permessi su questa classe')
        serializer.save()


class ListClasseTurnoInterrogazioneView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = models.ClasseTurnoInterrogazione.objects.all().order_by('-id')
    serializer_class = serializers.ClasseTurnoInterrogazioneSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    
    def perform_create(self, serializer):
        if serializer.validated_data['classe'].creatore != self.request.user: # Se non è il proprietario della room , non ha i permessi
            raise exceptions.PermissionDenied(
                detail='Non hai i permessi su questa classe')
        if serializer.is_valid():
            serializer.save()

class DetailClasseTurnoInterrogazioneView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ClasseTurnoInterrogazione.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = serializers.ClasseTurnoInterrogazioneSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    def perform_delete(self, serializer):
        if serializer.validated_data['classe'].creatore != self.request.user: # Se non è il proprietario della room , non ha i permessi
            raise exceptions.PermissionDenied(
                detail='Non hai i permessi su questa classe')
        serializer.save()



def my_view(request):
    id_classe = 2
    datas = []
    buffer_prevision = []
    ClasseTurnoInterrogazione_query = models.ClasseTurnoInterrogazione.objects.filter(classe=id_classe,stato=0).order_by('data')
    for turno in ClasseTurnoInterrogazione_query:
        buffer_this_prevision = []
        id_turno = turno.id
        materia_turno = turno.materia
        data = turno.data
        numero_interrogati = turno.numero_interrogati
        print("ID TURNO: "+str(id_turno))
        ClasseTurnoInterrogazione_close_query = models.ClasseTurnoInterrogazione.objects.filter(classe=id_classe,stato=1,materia=materia_turno).order_by('data')
        Profile_close_notconfirmed_queryset=[]
        for turno in ClasseTurnoInterrogazione_close_query:
            ProfileInterrogazione_close_notconfirmed_queryset = models_accounts.ProfileInterrogazione.objects.filter(turnointerrogazione=turno.id,conferma=0).values('profile')
            Profile_close_notconfirmed_queryset = models_accounts.Profile.objects.filter(pk__in=ProfileInterrogazione_close_notconfirmed_queryset)
            for profile in Profile_close_notconfirmed_queryset:
                print("PROFILE :"+str(profile))
                buffer_this_prevision.append(profile["id"])

        id_inbufferprevision= []
        for prev in buffer_prevision:
            id_inbufferprevision.append(prev["profile"])
        
        #if len(Profile_close_notconfirmed_queryset) > 0:
        buff_available = models_accounts.Profile.objects.filter(classe=id_classe).exclude(Q(pk__in=Profile_close_notconfirmed_queryset) | Q(pk__in=id_inbufferprevision))
        #else:
        #    buff_available = models_accounts.Profile.objects.filter(classe=id_classe).exclude(pk__in=id_inbufferprevision)

        
        print("DISPONIBILI: "+str(buff_available))
        print(str(turno.numero_interrogati))

        select_profile = models_accounts.ProfilePreferenzeMateria.objects.filter(profile__in=buff_available,materia=materia_turno).order_by('-valore').values('profile').distinct()[:numero_interrogati-len(buffer_this_prevision)]
        print("list SELECTED PROFILE :"+str(select_profile))
        for profile in select_profile:
            print("SELECTED PROFILE :"+str(profile))
            buffer_this_prevision.append(profile["profile"])
        
        for profile in buffer_this_prevision:
            print(str(profile)+str(id_turno)+str(data)+str(materia_turno))
            idmateriaturno = models.ClasseMateria.objects.filter(id=materia_turno.id).values('id')[0]["id"]
            dnome_materia = models.ClasseMateria.objects.filter(id=materia_turno.id).values('nome')[0]["nome"]
            first_name = models_accounts.Profile.objects.filter(id=profile).values('first_name')[0]["first_name"]
            last_name = models_accounts.Profile.objects.filter(id=profile).values('last_name')[0]["last_name"]
            avatar_image = models_accounts.Profile.objects.filter(id=profile).values('avatar_image')[0]["avatar_image"]
            buffer_prevision.append({'profile':profile,'first_name':first_name,'last_name':last_name,'avatar_image':avatar_image,'id_turno':id_turno,'data':data,'materia_turno':idmateriaturno,'nome_materia_turno':dnome_materia})
            #buffer_prevision.append([profile.id,profile.id,id_turno,data,materia_turno])
        
        #serializer = serializers.PianificazioniTurniSerializer(list(buffer_prevision),many=True)
        
    return JsonResponse({'previsioni':buffer_prevision},safe=False)

    #def list(self, request):
    #    queryset = self.get_queryset()
    #    # the serializer didn't take my RawQuerySet, so made it into a list
    #    serializer = serializers_accounts.ProfilePreferenzeMateriaSerializer(list(queryset), many=True)
    #    return Response(serializer.data)

#class PrevisioneInterrogazioni(generics.RetriveAPIView):
#    serializer_class = serializers.PrevisioneInterrogazioni
#    return models.ClasseTurnoInterrogazione.objects.filter(classe=2).order_by('id')[0:8]
    
