from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task-list")
    context = {"tasks":tasks, "form": form}
    return render(request, "task_list.html", context)

def task_update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task-list")
            
    context = {"form": form}
    return render(request, "task_list.html", context)

def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("task-list")
    context = {"task": task}
    return render(request, "task_delete.html", context)