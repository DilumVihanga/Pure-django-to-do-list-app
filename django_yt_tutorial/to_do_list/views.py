from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import addTaskForm
from .forms import CreateUserForm
from django.shortcuts import render


def home(request):
    
    obj = Tasks.objects.all()
    createTask = addTaskForm
    if request.method == "POST":
      form=addTaskForm(request.POST)
      if form.is_valid():
            form.save()
            
    context = {
        'items': obj,
        'form': createTask,
    }

  
    return render(request, 'home.html', context)


def login(request):
    
    return render(request, "login.html", {})


def register(request):
    create_user = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "register.html", {'form': create_user})