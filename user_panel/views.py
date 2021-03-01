from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def add_user(request):
    # user creations form
    form = UserCreationForm()
    return render(request, 'users/add_user.html', {'form': form})


def delete_user(request):
    pass
