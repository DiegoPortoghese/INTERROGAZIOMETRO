from django.shortcuts import render
from rest_framework import generics, viewsets, status, exceptions, filters
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from chatmessages import models
from . import permissions
from . import serializers

# Create your views here.
class ListChatMessageView(generics.ListCreateAPIView):
    queryset = models.ChatMessage.objects.all().order_by('-id')
    serializer_class = serializers.ChatMessageSerializer
    def get_queryset(self):
        return models.ChatMessage.objects.filter(from_user=self.request.user).order_by('-id') | models.ChatMessage.objects.filter(to_user=self.request.user).order_by('-id')
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    parser_classes = (MultiPartParser,)
    
    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

class DetailChatMessageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ChatMessage.objects.all()
    serializer_class = serializers.ChatMessageSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]


# Create your views here.
class ListGroupChatMessageView(generics.ListCreateAPIView):
    queryset = models.GroupChatMessage.objects.all().order_by('id')
    serializer_class = serializers.GroupChatMessageSerializer
    def get_queryset(self):
        return models.GroupChatMessage.objects.filter(group_id=self.kwargs['group_id']).order_by('id')
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    parser_classes = (MultiPartParser,)
    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

class ListGroupLimitChatMessageView(generics.ListCreateAPIView):
    queryset = models.GroupChatMessage.objects.all().order_by('id')[:7]
    serializer_class = serializers.GroupChatMessageSerializer
    def get_queryset(self):
        return models.GroupChatMessage.objects.filter(group_id=self.kwargs['group_id']).order_by('id')[:7]
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]
    parser_classes = (MultiPartParser,)
    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

class DetailGroupChatMessageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.GroupChatMessage.objects.all()
    serializer_class = serializers.GroupChatMessageSerializer
    permission_classes = [permissions.permissions.IsAuthenticatedOrReadOnly,]