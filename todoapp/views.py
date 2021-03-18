from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'all_tasks': tasks,
               'task_form': form,}

    return render(request, 'todoapp/index.html', context)


def about(request):
    return render(request, 'todoapp/about.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def complete_task(request, task_pk):
    task2 = Task.objects.get(id=task_pk)
    task2.completed = True
    task2.save()
    return redirect('index')

def delete_completed(request):
    completed_tasks = Task.objects.filter(completed = True)
    completed_tasks.delete()
    return redirect('index')

def delete_all(request):
    tasks = Task.objects.all()
    tasks.delete()
    return redirect('index')

def login(request):
    return render(request, 'todoapp/login.html')

def register(request):
    return render(request, 'todoapp/register.html')
