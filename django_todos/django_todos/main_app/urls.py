from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/create', views.todo_create, name='todo_create'),
]
