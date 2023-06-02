from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django_faculdade_site.apps.add_user.forms import AddUserForm
from django.contrib import messages

from django_faculdade_site.apps.cad_roupas.models import Funcionario


# Create your views here.

@login_required(login_url="/accounts/login/")
def add_user(req):
    if req.method == 'GET':
        form = AddUserForm()
        funcionarios = Funcionario.funcionario.all()
        return render(req, 'add_user/add_user.html', {'form': form, 'funcionarios': funcionarios})

    if req.method == 'POST':
        form = AddUserForm(req.POST)
        funcionarios = Funcionario.objects.all()
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(req, 'You have singed up successfully.')
            return redirect('/')
        else:
            return render(req, 'add_user/add_user.html',  {'form': form, 'funcionarios': funcionarios})

@login_required(login_url="/accounts/login/")
def rem_user(req, id_user):
    try:
        user = Funcionario.funcionario.get(id=id_user)
        user.delete()
    except Exception as error:
        print(error)

    return HttpResponseRedirect(f"/accounts/add_user/")