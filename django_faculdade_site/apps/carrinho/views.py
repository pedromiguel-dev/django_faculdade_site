from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django_faculdade_site.apps.cad_roupas.models import Carrinho, CarrinhoItem, Roupa


@login_required(login_url="/accounts/login/")
def carrinho(req):
    return render(
        request=req,
        template_name="carrinho/carrinho.html",
    )


@login_required(login_url="/accounts/login/")
def carrinho_info(req):
    carrinho_instance, _ = Carrinho.objects.get_or_create(pago=False, usuario=req.user)
    carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho_instance)

    carrinho_valor = sum([i.roupa.valor for i in carrinho_itens])
    lavagem_preco = sum([i.roupa.precoLavagem for i in carrinho_itens])

    return render(
        request=req,
        template_name="carrinho/carrinho_info.html",
        context={
            "carrinho_preco": carrinho_valor,
            "carrinho_lavagem": lavagem_preco,
            "carrinho_cheio": carrinho_itens
        },
    )


@login_required(login_url="/accounts/login/")
def carrinho_cards(req):
    carrinho_instance, _ = Carrinho.objects.get_or_create(pago=False, usuario=req.user)
    carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho_instance)

    return render(
        request=req,
        template_name="carrinho/carrinho_cards.html",
        context={
            "carrinho_items": carrinho_itens,
        },
    )


@login_required(login_url="/accounts/login/")
def carrinho_add(req, id_roupa):
    roupa = Roupa.objects.get(pk=id_roupa)
    tamanho = req.GET.get("tamanho")
    usuario = req.user
    carrinho_instance, _ = Carrinho.objects.get_or_create(usuario=usuario, pago=False)
    CarrinhoItem.objects.create(
        carrinho=carrinho_instance,
        roupa=roupa,
        tamanho=tamanho,
        quantidade=1,
    )

    return HttpResponseRedirect(f"/produto/{id_roupa}/")


@login_required(login_url="/accounts/login/")
def carrinho_del(req, id_roupa):
    try:
        item_carrinho = CarrinhoItem.objects.get(id=id_roupa)
        item_carrinho.delete()
    except Exception as error:
        print(error)

    return HttpResponseRedirect(f"/carrinho/")
