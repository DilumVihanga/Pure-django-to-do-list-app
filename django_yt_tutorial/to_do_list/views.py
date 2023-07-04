from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """ return HttpResponse("<h1>This is the home page</h1>") """
    my_tasks = list()

    my_tasks = list()

    if request.method == "POST":
        task = request.POST.get("task")
        my_tasks.append(task)

    context = {
        "tasks": my_tasks,
    }

    return render(request, 'home.html', context)


def login(request):
    """ return HttpResponse("<h1>This is the login page</h1>") """
    return render(request, "login.html", {})

def register(request):
    """ return HttpResponse("<h1>This is the register page</h1>") """
    return render(request, "register.html", {})
