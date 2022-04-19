from asyncio import Task
from django.forms import DateTimeInput, ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'day': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
