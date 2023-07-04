from django.db import models

# Create your models here.


class Tasks(models.Model):
    
    title = models.CharField(max_length=200)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)