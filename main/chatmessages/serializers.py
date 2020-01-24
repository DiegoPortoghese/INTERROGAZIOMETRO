from rest_framework import serializers
from chatmessages import models
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers as xxx
from drf_extra_fields.fields import Base64ImageField

import json


class ChatMessageSerializer(serializers.ModelSerializer):
    
    from_user_first_name = serializers.ReadOnlyField(source='from_user.first_name')
    from_user_last_name = serializers.ReadOnlyField(source='from_user.last_name')
    
    to_user_first_name = serializers.ReadOnlyField(source='to_user.first_name')
    to_user_last_name = serializers.ReadOnlyField(source='to_user.last_name')

    class Meta:
        fields = (
            'id',
            'from_user',
            'to_user',
            'from_user_first_name',
            'from_user_last_name',
            'to_user_first_name',
            'to_user_last_name',
            'message',
            'creation_date',
            'displayed',
        
        )
        model = models.ChatMessage


class GroupChatMessageSerializer(serializers.ModelSerializer):
    from_user_first_name = serializers.ReadOnlyField(source='from_user.profile.first_name')
    from_user_last_name = serializers.ReadOnlyField(source='from_user.profile.last_name')

    class Meta:
        fields = (
            'id',
            'group_id',
            'from_user',
            'from_user_first_name',
            'from_user_last_name',
            'message',
            'creation_date'        
        )
        model = models.GroupChatMessage
