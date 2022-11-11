# Django Stuff
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.staticfiles import views
import random

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

currentTabId = 0


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
    if selRoom['id'] == 'math':
        randomMath()
    # TODO: Add Math Executive to the context parameter below:>
    context = {'rooms': rooms, 'athRandomSet': Temporary}
    return render(request, 'base/subjects/room.'+selRoom['id']+'.html', context)


# TODO: Add this to HTML :)
Temporary = []
Temporary = {}
numberOfRandom = 0
MathQuestionNum = 0


def randomMath():
    global MathQuestionNum
    # breakpoint()
    for i in range(10):
        Temporary = {}

        Temporary['options'] = []
        Temporary['number'] = []
        Temporary['operator'] = []
        Temporary['answer'] = 0
        Temporary['question'] = ''

        numberOfRandom = random.randint(2, 5)

        for j in range(numberOfRandom):
            Temporary['number'].append(random.randint(0, 50))
        for j in range(numberOfRandom-1):
            Temporary['operator'].append(random.randint(0, 3))
        # 0:+, 1:-, 2:*, 3:/
        Temporary['answer'] = Temporary['number'][0]
        for j in range(1, numberOfRandom):
            if Temporary['operator'][j-1] == 0:
                Temporary['answer'] += Temporary['number'][j]
            if Temporary['operator'][j-1] == 1:
                Temporary['answer'] -= Temporary['number'][j]
            if Temporary['operator'][j-1] == 2:
                Temporary['answer'] *= Temporary['number'][j]
            if Temporary['operator'][j-1] == 3:
                if Temporary['number'][j] == 0:
                    Temporary['answer'] /= Temporary['number'][j]+1
                    Temporary['number'][j] += 1
                else:
                    Temporary['answer'] /= Temporary['number'][j]
        Temporary['question'] = str(Temporary['number'][0])
        for j in range(len(Temporary['operator'])):
            if Temporary['operator'][j] == 0:
                Temporary['question'] += "+"
                Temporary['question'] += str(
                    Temporary['number'][j+1])
            if Temporary['operator'][j] == 1:
                Temporary['question'] += "-"
                Temporary['question'] += str(
                    Temporary['number'][j+1])
            if Temporary['operator'][j] == 2:
                Temporary['question'] += "*"
                Temporary['question'] += str(
                    Temporary['number'][j+1])
            if Temporary['operator'][j] == 3:
                Temporary['question'] += "/"
                Temporary['question'] += str(
                    Temporary['number'][j+1])
        # breakpoint()
        for j in range(3):
            Temporary['options'].append(random.randint(
                int(Temporary['answer'])-10, int(Temporary['answer'])+10))
        Temporary['options'].append(Temporary['answer'])
        MathQuestionNum.append(Temporary)
        # MathRandomSet is a variable :)
    MathQuestionNum = len(Temporary)
