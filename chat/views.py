from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.

def home(request):
    return render(request, 'home.html')


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)

def room(request, room):
    room_details = Room.objects.get(name=room)
    username = request.GET['username']
    return render(request, 'room.html',
                {'username':username,
                 'room':room,
                 'room_details':room_details})