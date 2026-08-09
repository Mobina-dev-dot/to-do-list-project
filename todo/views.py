from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'todo/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(user=request.user)
    return render(request, 'todo/task_form.html', {'form': form})

@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task, user=request.user)
    return render(request, 'todo/task_form.html', {'form': form})

@login_required
def task_toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    task.delete()
    return redirect('task_list')