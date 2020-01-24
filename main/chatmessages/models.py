from django.db import models

from django.utils.translation import ugettext_lazy as _

# Create your models here.

class ChatMessage(models.Model):
    from_user = models.ForeignKey('auth.User', related_name='message_from', on_delete=models.CASCADE, default=1)
    to_user = models.ForeignKey('auth.User', related_name='message_to', on_delete=models.CASCADE, default=1)
    message = models.TextField(default='')
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    displayed = models.BooleanField(verbose_name=_(u"Visualizzato"),default=False)
    
    def __str__(self):
        return self.message

class GroupChatMessage(models.Model):
    group_id = models.ForeignKey('classi.Classe', related_name='group_chat', on_delete=models.CASCADE, default=1)
    from_user = models.ForeignKey('auth.User', related_name='group_message_from', on_delete=models.CASCADE, default=1)
    message = models.TextField(default='')
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.message