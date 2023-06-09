import locale

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm

def sign_up(req):
    if req.method == 'GET':
        form = RegisterForm()
        return render(req, 'registration/cadastro.html', {'form': form})

    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(req, 'You have singed up successfully.')
            login(req, user)
            return redirect('/')
        else:
            return render(req, 'registration/cadastro.html', {'form': form})


def sign_in(req):
    if req.method == 'GET':
        form = LoginForm()
        return render(req, 'registration/login.html', {'form': form})
