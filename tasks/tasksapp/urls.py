from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /tasks/5/
    path('<int:task_id>/', views.detail, name='detail'),
]