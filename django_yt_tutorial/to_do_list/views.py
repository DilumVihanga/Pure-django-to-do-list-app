from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import addTaskForm


""" my_tasks= list() """

def home(request):
    """ return HttpResponse("<h1>This is the home page</h1>") """
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

    """ if request.method == "POST":
        task = request.POST.get("task")
        my_tasks.append(task)

    context = {
        "tasks": my_tasks,
    }
 """
    return render(request, 'home.html', context)


def login(request):
    """ return HttpResponse("<h1>This is the login page</h1>") """
    return render(request, "login.html", {})

from .forms import CreateUserForm

def register(request):
    create_user = CreateUserForm()
    return render(request, "register.html", {'form': create_user})
