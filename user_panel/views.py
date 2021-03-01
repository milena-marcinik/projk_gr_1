from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserAddForm


def add_user(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')  # te wiadomosci dodać potem to template BASE jak juz bedzie
            return redirect('login')
    else:
        form = UserAddForm()
    return render(request, 'user_panel/add_user.html', {'form': form})


def delete_user(request):
    pass
