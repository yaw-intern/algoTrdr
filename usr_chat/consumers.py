from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
import json
from .models import Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def create_chat(self, msg, sender, receiver):
        return Message.objects.create(sender=sender, receiver=receiver, content=msg)

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        # Get the current user and display their username
        self.user = await self.get_user()
        username = self.user.username if self.user.is_authenticated else 'Anonymous'

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        username = self.user.username if self.user.is_authenticated else 'Anonymous'

        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        #create new chat object
        chat = Message(
            content = message,
            sender=self.scope['user'],
            recipient = self.scope['user'],
        )

        await database_sync_to_async(chat.save)()

        # Send message to room group
       
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'username': username,
            'message': message
        }))

    @database_sync_to_async
    def get_user(self):
        # Retrieve the current user from the database
        return User.objects.get(pk=self.scope["user"].id)

    
