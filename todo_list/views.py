from django.shortcuts import render, redirect
from .forms import TaskForm, TaskUpdateForm
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(title=form.cleaned_data['title'], description=form.cleaned_data['description'], user=request.user)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        return render(request, 'add_task.html', {'form': form})
    
@login_required
def list_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})
        
@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to task list page
    else:
        form = TaskUpdateForm(instance=task)
    return render(request, 'update_task.html', {'form': form})

@login_required
def remove_task(request, task_id):
    if (request.method == 'POST'):
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
    
    return list_tasks(request)

