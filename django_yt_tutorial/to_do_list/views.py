from django.shortcuts import render
from django.http import HttpResponse
from .models import *

""" my_tasks= list() """

def home(request):
    """ return HttpResponse("<h1>This is the home page</h1>") """
    obj = Tasks.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        date = request.POST.get("date")
        time = request.POST.get("time")
        obj = Tasks(Title=title, Date=date, Time=time)
       
    context = {
        'items': obj,
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

def register(request):
    """ return HttpResponse("<h1>This is the register page</h1>") """
    return render(request, "register.html", {})
