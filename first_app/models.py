from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskTitle  = models.CharField(max_length=30,primary_key=True)
    taskDescription  = models.TextField(max_length=300)
    is_completed = models.BooleanField(default=False)
    
    