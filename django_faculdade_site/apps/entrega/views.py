from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django_faculdade_site.apps.cad_roupas.models import Carrinho, CarrinhoItem, Pedido


# Create your views here.
@login_required(login_url="/accounts/login/")
def entrega(req):
    return render(
        request=req,
        template_name="entrega/entrega.html",
    )


def entrega_info(req):
    carrinho_instance, _ = Carrinho.objects.get_or_create(usuario=req.user, pago=False )
    carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho_instance)
    carrinho_valor = sum([i.roupa.valor for i in carrinho_itens])
    lavagem_preco = sum([i.roupa.precoLavagem for i in carrinho_itens])

    return render(
        request=req,
        template_name="entrega/entrega_info.html",
        context={
            "carrinho_preco": carrinho_valor,
            "carrinho_lavagem": lavagem_preco,
            "carrinho_cheio": carrinho_itens
        },
    )


@login_required(login_url="/accounts/login/")
def entrega_reg(req):
    numero_telefone = req.GET.get("numero_telefone")
    carrinho_instance = Carrinho.objects.get(pago=False, usuario=req.user)
    carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho_instance)

    carrinho_valor = sum([i.roupa.valor for i in carrinho_itens])
    lavagem_preco = sum([i.roupa.precoLavagem for i in carrinho_itens])
    total = carrinho_valor + lavagem_preco

    if carrinho_valor <= 0 or len(numero_telefone) <= 0:
        return HttpResponseRedirect("/")

    try:
        Pedido.objects.create(
            usuario=req.user,
            carrinho=carrinho_instance,
            preco_total=total,
            numero_cliente=numero_telefone
        )
        carrinho_instance.pago = True
        carrinho_instance.save()
    except Exception as error:
        return HttpResponseServerError(error)

    return HttpResponseRedirect("/agradecimento/")


def agradecimento(req):
    return render(
        request=req,
        template_name="entrega/agradecimento.html",
    )
