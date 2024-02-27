from django.shortcuts import render,redirect
from first_app.models import TaskModel
from .forms import AddTaskForm
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class HomeTemplate(TemplateView):
    template_name = 'home.html'
    
class TodoForm(CreateView):
    model = TaskModel
    template_name = 'add_task.html'
    form_class = AddTaskForm
    success_url = reverse_lazy('show_tasks')
    
class TaskListView(ListView):
    model = TaskModel
    template_name = 'show_tasks.html'
    context_object_name = 'tasklist'
    
class TaskUpdate(UpdateView):
    form_class = AddTaskForm
    model = TaskModel
    template_name = 'add_task.html'
    success_url = reverse_lazy('show_tasks')
    
class DeleteTask(DeleteView):
    model = TaskModel
    template_name = 'dlt_conf.html'
    success_url = reverse_lazy('show_tasks')
    
class MoveToCompletedView(View):
    def get(self, request, **kwargs):  # Adjust the arguments here
        pk = kwargs.get('pk')
        task = TaskModel.objects.get(pk=pk)
        task.is_completed = True
        task.save()
        return redirect('completed')
    success_url = reverse_lazy('completed')

class CompletedTask(ListView):
    model = TaskModel
    template_name = 'completed.html'
    context_object_name = 'tasklist'