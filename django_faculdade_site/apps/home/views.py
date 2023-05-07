from django.shortcuts import render

from django_faculdade_site.apps.cad_roupas.models import Categoria


# Create your views here.
def home(req):
    return render(
        request=req, template_name="home/home.html"
    )


