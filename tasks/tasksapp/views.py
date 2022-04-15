from asyncio import tasks
from re import template
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Task
from django.views import generic


def index(request):
    list_of_tasks = Task.objects.all()
    context = {
        'list_of_tasks': list_of_tasks,
    }
    return render(request, 'tasksapp/index.html', context)

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasksapp/detail.html", {'task': task})

class IndexView(generic.ListView):
    template_name = 'tasksapp/index.html'
    context_object_name = 'list_of_tasks'

    def get_queryset(self):
        return Task.objects.all()
    
