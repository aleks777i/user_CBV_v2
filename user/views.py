from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from .models import User
from .forms import UserForm


class UserListView(ListView):

    model = User
    template_name = 'index.html'
    context_object_name = 'users'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = User.objects.all().count()
        return context


class UserDetailView(DetailView):

    model = User
    template_name = 'user.html'
    context_object_name = 'user'


class UserAddView(CreateView):
    model = User
    fields = ['username', 'email']
    template_name = 'add_user.html'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('home')


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'update_user.html'


