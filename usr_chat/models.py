from django.db import models
from django.contrib.auth import get_user_model
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
# Create your models here.
class Message(models.Model):
    User = get_user_model()
    sender = models.ForeignKey(get_user_model(), related_name="author_messages", on_delete=models.CASCADE)
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_messages', default=9)
    content = models.TextField()
    senderUsername = models.TextField()
    roomid = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.author.username
    
    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:30]