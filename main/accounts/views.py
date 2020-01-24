from rest_auth.registration.views import RegisterView
from rest_auth.app_settings import TokenSerializer
from accounts.serializers import CustomPasswordResetSerializer
from rest_auth.views import PasswordResetView
from allauth.account.utils import complete_signup
from accounts.models import Profile
from rest_auth.app_settings import create_token
from allauth.account import app_settings as allauth_settings
from rest_framework import generics, viewsets, status, exceptions, filters
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers
from . import permissions
#from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CustomRegisterView(RegisterView):
    """
    Override della view di registrazione di rest-auth 
    per fare in modo di ricevere il token per loggare lo user 
    automaticamente dopo la registrazione anche con l'opzione mandatory.
    """

    def get_response_data(self, user):
        return TokenSerializer(user.auth_token).data

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        create_token(self.token_model, user, serializer)
        complete_signup(self.request._request, user,
                        allauth_settings.EMAIL_VERIFICATION,
                        None)
        
        # creo il profilo utente
        Profile.objects.create(user=user)

        return user

class DetailProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileUserDetailsSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly,]
    
class ListProfilePreferenzeMateriaView(generics.ListCreateAPIView):
    queryset = models.ProfilePreferenzeMateria.objects.all()
    serializer_class = serializers.ProfilePreferenzeMateriaSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]

class DetailProfilePreferenzeMateriaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProfilePreferenzeMateria.objects.all()
    serializer_class = serializers.ProfilePreferenzeMateriaSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]


class ListProfileInterrogazioneView(generics.ListCreateAPIView):
    queryset = models.ProfileInterrogazione.objects.all()
    serializer_class = serializers.ProfileInterrogazioneSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]

class DetailProfileInterrogazioneView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProfileInterrogazione.objects.all()
    serializer_class = serializers.ProfileInterrogazioneSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]



# class custompasswordresetview(passwordresetview):
#     """
#     calls django auth passwordresetform save method.

#     accepts the following post parameters: email
#     returns the success/fail message.
#     """
#     serializer_class = custompasswordresetserializer