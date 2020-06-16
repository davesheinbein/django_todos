from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def home(request):
    return render(request, 'main_app/home.html', {
        'todos': Todo.objects.all() 
    })

def todo_create(request):
    Todo.objects.create(todo_text=request.POST['todo_text'])
    return redirect('home')