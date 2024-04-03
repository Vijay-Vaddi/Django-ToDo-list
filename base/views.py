'''For testing class base views'''
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

'''CRUD views'''
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

'''To Login and retrict pages'''
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

'''To register and login directly'''
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 

from django.urls import reverse_lazy
from .models import Task

# Create your views here.

class UserLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__" 
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')


class RegisterUser(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)


class TaskList(LoginRequiredMixin, ListView):
    
    model = Task
    context_object_name = 'tasks' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count() 

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):

    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')