from audioop import reverse
from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

todo_tasks = [
    {'id':1,'name': 'task1', 'description': 'doing some steps to finish task no 1', 'state': False, },
    {'id':2,'name': 'task2', 'description': 'doing some steps to finish task no 2', 'state': False },
    {'id':3,'name': 'task3', 'description': 'doing some steps to finish task no 3','state': False},
    {'id':4,'name': 'task4', 'description': 'doing some steps to finish task no 4','state': False},
    {'id':5,'name': 'task5', 'description': 'doing some steps to finish task no 5','state': False}

]
def index(request):
    context={
        'todos': todo_tasks
    }
    return render(request, 'todo/index.html', context)

def todo_details(request, id):
    todo = [todo for todo in todo_tasks if todo['id'] == id]
    context={
        'todo':todo[0]
    }
    return render(request,'todo/details.html',context)

def todo_done(request, id):
    todo = [todo for todo in todo_tasks if todo['id'] == id]
    if todo[0]['state']==True:
        todo[0]['state']=False
    else:
        todo[0]['state']=True
    
    return redirect(reverse('todo:list'))

def update_todo(request,id):
    todo = [todo for todo in todo_tasks if todo['id'] == id]

    if request.method == 'POST':
        todo[0]['name']=request.POST['taskname']
        todo[0]['description']=request.POST['description']
        if 'task-state' in request.POST:
            todo[0]['state']=True
        else:
            todo[0]['state']=False
        return redirect(reverse('todo:list'))

           
    context={
        'todo':todo[0]
    }
    return render(request, 'todo/update.html',context)

def delete_task(request,id):
    todo = [todo for todo in todo_tasks if todo['id'] == id]
    todo_tasks.remove(todo[0])
    return redirect(reverse('todo:list'))

def finished_tasks(request):
    finished_tasks = [todo for todo in todo_tasks if todo['state'] == True]
    context={
        'todos': finished_tasks
    }
    return render(request, 'todo/finished.html',context)

def unfinished_tasks(request):
    unfinished_tasks = [todo for todo in todo_tasks if todo['state'] == False]
    context={
        'todos': unfinished_tasks
    }
    return render(request, 'todo/unfinished.html',context)
