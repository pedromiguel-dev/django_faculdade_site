from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from django_faculdade_site.apps.cad_roupas.models import Pedido


# Create your views here.

@login_required(login_url="/accounts/login/")
def perfil(req):
    perfil_user_email = req.user.email
    perfil_user_name = User.get_username(req.user)
    pedidos = Pedido.objects.select_related().filter(usuario=req.user)
    pedidos_pagos = []

    for pedido in pedidos:
        if not pedido.carrinho.pago:
            continue
        pedidos_pagos.insert(0, pedido)

    return render(
        request=req,
        template_name="perfil/perfil.html",
        context={
            "email": perfil_user_email,
            "name": perfil_user_name,
            "image": "cat-img.png",
            "pedidos_pagos": pedidos_pagos
        }
    )
