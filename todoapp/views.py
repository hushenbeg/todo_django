from django.shortcuts import render, redirect
from .models import AddTask
from django.core.exceptions import SuspiciousOperation

# Create your views here.

def index(request):

    return render(request,'todoapp/index.html')

def add_task(request):

    if request.method == 'POST':
        name = request.POST.get("name","")
        priority = request.POST.get("priority", "")
        
        add_items = AddTask(name=name, priority=priority)

        add_items.save()

    return render(request, 'todoapp/add_task.html')

def view_task(request):

    view_items = AddTask.objects.all()

    return render(request, 'todoapp/view.html', {'view_items':view_items})

def delete_task(request, id):

    task = AddTask.objects.get(id=id)

    context = {
        'task':task,
    }

    if request.method == 'POST':
        task.delete()
        return redirect('/todoapp/view_task')

    return render(request, 'todoapp/delete.html', context)


def update_task(request, id):

    update_items = AddTask.objects.get(id=id)

    if request.method=='POST':
        update_items.name = request.POST.get("name","")
        update_items.priority = request.POST.get("priority","")
        update_items.save()
        return redirect('/todoapp/view_task')
    
    context = {
        'update_items':update_items
    }

    return render(request, 'todoapp/update.html', context)
