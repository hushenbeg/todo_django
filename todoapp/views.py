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

    delete_items = AddTask.objects.get(id=id)

    delete_items.delete()

    return render(request, 'todoapp/delete.html', {'delete_items':delete_items})

def update_task(request, id):

    update_items = AddTask.objects.get(id=id)

    if request.method=='POST':
        update_items.name = request.POST.get("name","")
        update_items.priority = request.POST.get("priority","")
        update_items.save()
        redirect('todoapp/view.html')

    return render(request, 'todoapp/update.html', {'update_items': update_items})
