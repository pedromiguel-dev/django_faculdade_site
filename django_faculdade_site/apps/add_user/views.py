from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django_faculdade_site.apps.cad_roupas.models import User


# Create your views here.

@login_required(login_url="/accounts/login/")
def add_user(req):
    if req.user.role != User.Role.ADMIN:
        return HttpResponseRedirect("/")

    perfil_user_email = req.user.email
    perfil_user_name = User.get_username(req.user)
    user_role = req.user.role

    return render(
        request=req,
        template_name="perfil/perfil.html",
        context={
            "email": perfil_user_email,
            "name": perfil_user_name,
            "image": "cat-img.png",
            "pedidos_pagos": [],
            "role": user_role
        }
    )
