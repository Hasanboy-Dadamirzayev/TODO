from django.shortcuts import render, redirect
from main.models import *

def home_view(request):
    if request.method == 'POST':
        Todo.objects.create(
            nom = request.POST.get('nom'),
            batafsil = request.POST.get('batafsil'),
        )
    notes = Todo.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'index.html', context)

def todo_vew(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo
    }
    return render(request, 'todo.html', context)

def todo_delet_view(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')