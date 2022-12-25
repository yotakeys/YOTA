# from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todolist/task_list.html'
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search = self.request.GET.get('search')
        if search:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search)
        context['search_value'] = search
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks')
    template_name = 'todolist/task_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'todolist/task_update.html'

    def test_func(self):
        return str(self.request.user.get_username()) == str(self.get_object().user) # noqa: E501


class TaskDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'todolist/task_delete.html'

    def test_func(self):
        return str(self.request.user.get_username()) == str(self.get_object().user) # noqa: E501
