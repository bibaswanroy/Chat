from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')


def checkview(request):
    room = request.POST['room_name'].strip()
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

def getMessages(request,room,username):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages':list(messages.values()),"username":username})

def sendMessages(request):
    room_id = request.POST['room_id']
    username = request.POST['username']
    message = request.POST['message']
    # if message == '':
    #     return render(request, 'room.html',{'alert':"Message body cannot be empty"})
    
    new_message = Message.objects.create(username=username,room=room_id,value=message)
    new_message.save()

    
