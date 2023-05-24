from django.shortcuts import render,redirect
from .models import *
from .forms import TaskForm

def update(request,task_id):
    task = Task.objects.get(pk = task_id)
    form = TaskForm(request.POST or None , instance=task)
    if form.is_valid():
        form.save()
        return redirect('main')
    return render(request , 'update.html' ,{'task':task , 'form':form})
def delete(request,task_id):
    task = Task.objects.get(pk = task_id)
    task.delete()
    return redirect('main')
def finish(request,task_id):
    task = Task.objects.get(pk = task_id)
    task.done = True
    task.save()
    return redirect('main')
   

def index(request):
    list = Task.objects.all()
    listForm = TaskForm()
    if request.method == "POST":
        listForm = TaskForm(request.POST)
        listForm.save()
        return redirect('/')
    context = {
        'tasks':list,
        'form' :listForm
    }
    return render(request , 'index.html' , context)
# Create your views here.
