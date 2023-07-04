from django.contrib import admin
from .models import Tasks

# Register your models here.

admin.site.register(Tasks)

def str_tasks(self):
    return self.title