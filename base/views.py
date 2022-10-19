

# Django Stuff
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.staticfiles import views

# Create your views here.
rooms = [
    {'id': 'english', 'name': 'English', 'priority': 1, 
    'subdir': ['Dictionary', 'Translator']},
    {'id': 'math', 'name': 'Math', 'priority': 1, 
    'subdir': ['Calculator', 'Convertor', 'Graphs']},
    {'id': 'literature', 'name': 'Literature', 'priority': 1, 
    'subdir': ['Examples Literature', 'Other...']},
    {'id': 'geometry', 'name': 'Geometry', 'priority': 2, 
    'subdir': ['World Map', 'Other Maps']},
    {'id': 'history', 'name': 'History', 'priority': 3, 
    'subdir': ['Other...']},
    {'id': 'biology', 'name': 'Biology', 'priority': 3, 
    'subdir': ['Other...']},
    {'id': 'technology', 'name': 'Technology', 'priority': 3, 
    'subdir': ['Other...']}
]
def rootToHome(request):
    return redirect('home')

def staticfile(request):
    views.server(request)



def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    selRoom = None
    for i in rooms:
        if i['id'] == str(pk):
            selRoom = i
    context = {'room': room}
    url = 'base/subjects/room.'+selRoom['id']+'.html'
    return render(request, url, context)
