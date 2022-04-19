from audioop import reverse
from re import template
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from .models import Task
from django.views import generic
from .forms import TaskForm


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
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            # hacer algo más con la nueva tarea o modificar algún atributo
            new_task.save() 
            return HttpResponseRedirect('/tasks')
    else:
        form = TaskForm()
    return render(request, "tasksapp/new_task.html", {'form': form})

class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = '__all__'
    template_name_suffix = '_update_form'
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/tasks/"



    
