from django.shortcuts import render
from random import randint
from .models import Message

def index(request):
    return render(request, 'frontend/index.html')

def room(request, room_name):
    messages = Message.objects.filter(room=room_name)[0:25]

    if request.user.is_authenticated:
        # use existing username
        username = request.user.username
    else:
        # generate random guest username
        username = 'guest' + ''.join([str(randint(0, 9)) for i in range(8)])

    return render(request, 'frontend/room.html', {'room_name': room_name, 'username': username, 'messages': messages})
