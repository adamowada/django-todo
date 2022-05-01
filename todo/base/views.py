import imp
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.

# looks for <model name>_list.html
class TaskList(ListView):
    model = Task
    context_object_name = "tasks"


# looks for <model name>_detail.html
class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "base/task.html"


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")  # after post, send user back to home

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")

class DeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")