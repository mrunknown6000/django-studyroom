from turtle import settiltangle
from urllib import response
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.staticfiles import views

# Create your views here.
rooms = [
    {'id': 'english', 'name': 'English'},
    {'id': 'math', 'name': 'Math'},
    {'id': 'literature', 'name': 'Literature'}
]

def rootToHome(request):
    return redirect('home')

def staticfile(request):
    views.server(request)



def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == str(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
