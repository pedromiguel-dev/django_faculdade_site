import locale

from django.shortcuts import render

from django_faculdade_site.apps.roupa.models import Roupa

locale.setlocale(locale.LC_ALL, "")


# Create your views here.

def roupa(req, id_roupa):
    roupa_instance = Roupa.objects.get(pk=id_roupa)
    roupas_rel = Roupa.objects.select_related().filter(categoria=roupa_instance.categoria)

    return render(
        request=req,
        template_name="roupa/roupa.html",
        context={
            "roupa": roupa_instance,
            "relacionados": roupas_rel,
            "preco": locale.currency(roupa_instance.valor, grouping=True),
        },
    )
