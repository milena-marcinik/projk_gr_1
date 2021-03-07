from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DeleteView
from django.contrib.auth.models import User

from .forms import UserAddForm
from .models import UserProfile


def add_user(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Account created for {username}!')  # te wiadomosci dodać potem to template BASE jak juz bedzie
            return redirect('login')
    else:
        form = UserAddForm()
    return render(request, 'user_panel/add_user.html', {'form': form})


class UserListView(ListView):
    model = User
    context_object_name = 'users_all'  # your own name for the list as a template variable
    queryset = User.objects.all()
    template_name = 'user_panel/users_all.html'  # Specify your own template name/location


class UserDeleteView(DeleteView):
    model = User
    success_url = '/users/'
