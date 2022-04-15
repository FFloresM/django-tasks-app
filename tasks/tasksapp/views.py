from asyncio import tasks
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Task


def index(request):
    list_of_tasks = Task.objects.all()
    context = {
        'list_of_tasks': list_of_tasks,
    }
    return render(request, 'tasksapp/index.html', context)

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasksapp/detail.html", {'task': task})
