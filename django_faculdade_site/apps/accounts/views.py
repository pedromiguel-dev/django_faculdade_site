from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, RegisterRoupa, RegisterCategoria


def sign_up(req):
    if req.method == 'GET':
        form = RegisterForm()
        return render(req, 'registration/cadastro.html', {'form': form})

    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
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
    
    
    
def register_roupa(req):
    print(req.POST,
          req.FILES)
    if req.method == "POST":
        form = RegisterRoupa(req.POST, req.FILES)
        form.base_fields
        if form.is_valid():
            form.save()
            messages.success(req, ('Your movie was successfully added!'))
        else:
            messages.error(req, 'Error saving form')
            print(form)
        
        
        return redirect("/")

    if req.method == 'GET':
        form = RegisterRoupa()
        return render(req, 'funcionario/funcionario.html', {'form': form})
    
    
def register_categoria(req):
    print(req.POST,
          req.FILES)
    if req.method == "POST":
        form = RegisterCategoria(req.POST, req.FILES)
        form.base_fields
        if form.is_valid():
            form.save()
            messages.success(req, ('Your movie was successfully added!'))
        else:
            messages.error(req, 'Error saving form')
            print(form)
        
        
        return redirect("/")

    if req.method == 'GET':
        form = RegisterCategoria()
        return render(req, 'categoria/cadastro.html', {'form': form})