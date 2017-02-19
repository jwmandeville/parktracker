from django.contrib.auth import views
from .forms import NewUserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def add_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(True)
            username = request.POST['username']
            password = request.POST['password2']
            authed_user = authenticate(username=username, password=password)
            if authed_user is not None:
                login(request, authed_user)
            else:
                print("user not authenticated")
            return redirect('home')
    else:
        form = NewUserForm()

    return render(request, 'registration/new_user.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')