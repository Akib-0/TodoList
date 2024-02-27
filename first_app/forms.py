from django import forms
from first_app.models import TaskModel

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle','taskDescription']