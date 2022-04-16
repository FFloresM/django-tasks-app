from audioop import reverse
from re import template
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
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

def newTask(request):
    if request.method == "POST":
        task = Task(
            text = request.POST['text'],
            day = request.POST['day'],
        )
        try:
            if request.POST['reminder'] == 'on':
                reminder = True 
        except KeyError:
            reminder = False
        task.reminder = reminder
        task.save()
        return HttpResponseRedirect(render(request, 'tasks:index'))
    else:
        return render(request, "tasksapp/new_task.html")



    
