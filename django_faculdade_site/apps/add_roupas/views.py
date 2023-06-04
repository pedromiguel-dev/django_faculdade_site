import locale

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterRoupa, RegisterCategoria, EditRoupa
from ..roupa.models import Roupa


@login_required(login_url="/accounts/login/")
def edit_roupa(req, id_roupa):
    if req.method == 'GET':
        roupa_instance = Roupa.objects.get(pk=id_roupa)
        roupas_rel = Roupa.objects.select_related().filter(categoria=roupa_instance.categoria)

        form = EditRoupa(instance=roupa_instance)
        return render(
            request=req,
            template_name="roupa/roupa_edit.html",
            context={
                "roupa": roupa_instance,
                "relacionados": roupas_rel,
                "preco": locale.currency(roupa_instance.valor, grouping=True),
                "form": form
            },
        )

    if req.method == 'POST':
        roupa_instance = Roupa.objects.get(pk=id_roupa)
        form = EditRoupa(req.POST, req.FILES, instance=roupa_instance)
        if form.is_valid():
            form.save()
            return redirect(f'/roupa/{id_roupa}')
        else:
            messages.error(req, 'Please correct the following errors:')
            return render(req, 'roupa/roupa_edit.html', {'form': form})


@login_required(login_url="/accounts/login/")
def rem_roupa(req, id_roupa):
    if req.method == 'GET':
        try:
            item_carrinho = Roupa.objects.get(pk=id_roupa)
            item_carrinho.delete()
            return HttpResponseRedirect(f"/categoria/reach/{item_carrinho.categoria.id}")
        except Exception as error:
            print(error)
            return HttpResponseRedirect("/")


@login_required(login_url="/accounts/login/")
def register_roupa(req):
    if req.method == "POST":
        form = RegisterRoupa(req.POST, req.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.error(req, 'Error saving form')

        return redirect("/funcionario/roupa")

    if req.method == 'GET':
        form = RegisterRoupa()
        roupas = Roupa.objects.all()
        return render(req, 'funcionario/funcionario.html', {'form': form, 'roupas': roupas})


@login_required(login_url="/accounts/login/")
def register_categoria(req):
    if req.method == "POST":
        form = RegisterCategoria(req.POST, req.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.error(req, 'Error saving form')
            print(form)

        return redirect("/")

    if req.method == 'GET':
        form = RegisterCategoria()
        return render(req, 'categoria/cadastro.html', {'form': form})
