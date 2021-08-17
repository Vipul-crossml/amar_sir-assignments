
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *
from .models import Task
# Create your views here.
"""
Index function is used to sent a post request,
to the db and fetch every task object
"""

def index(request):
    tasks = Task.objects.all()
    
    form = TaskForm()

    if request.method == 'POST':
        print(request.POST)

        title = request.POST.get('title')
        Task(name=title).save()
      

        return redirect('/')

    else:
        context = {'tasks': tasks, 'form': form}
        return render(request, 'todoapp/ui.html', context)
"""
Update task is used to get items,
 by primary key to change status.
"""
    


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'todoapp/update_task.html', context)

"""
DeleteTask will get item by primary key,
and delete instance of that object from DB.
"""


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'todoapp/delete.html', context)
