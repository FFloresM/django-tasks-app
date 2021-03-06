from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /tasks/5/
    path('<int:task_id>/', views.detail, name='detail'),
    path("new-task/", views.newTask, name='new-task'),
    path('<int:pk>/update', views.TaskUpdateView.as_view(), name='update'),
]