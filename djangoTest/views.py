from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('task_list')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})