from django.shortcuts import render

from django_faculdade_site.apps.cad_roupas.models import Categoria, Roupa


# Create your views here.
def categoria(req, cat):
    categoria_instance = Categoria.objects.get(id=cat)
    roupas = Roupa.objects.select_related().filter(categoria=cat)

    return render(
        request=req,
        template_name="categoria/categoria.html",
        context={
            "categoria": categoria_instance,
            "roupas": roupas,
        },
    )


def categorias_cards(req):
    if req.method == 'GET':
        categorias = Categoria.objects.all()

        return render(
            request=req, template_name="home/categorias_cards.html", context={"categorias": categorias}
        )
