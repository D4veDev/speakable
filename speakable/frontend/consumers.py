import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import detectlanguage
import requests
from .models import Message

detectlanguage.configuration.api_key = "cd27306754d4dbec8bf30e6e4236cf24"

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
        language = detectlanguage.simple_detect(message)
        data = {
            'text': message,
            'mode': 'standard',
            'lang': language,
            'opt_countries': 'us,gb,fr',
            'api_user': '831118967',
            'api_secret': 'XGiBggqNDs29e7wsMuCy'
        }

        # if message language is supported by sightengine
        if language in ('en', 'zh', 'nl', 'de', 'it', 'pt', 'es', 'sv', 'tl'):
            # ask sightengine, what it thinks about the message
            r = requests.post('https://api.sightengine.com/1.0/text/check.json', data=data)
            output = json.loads(r.text)
            
            # censor the message, if it contains inappropriate content
            if output["profanity"]["matches"]: message = "This message contains profanity"
            # if output["personal"]["matches"]: message = "This message contains personal information"
            # if output["link"]["matches"]: message = "This message contains a link"

        # save message to database
        await self.save_message(username, room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )
    
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        Message.objects.create(username=username, room=room, content=message)
