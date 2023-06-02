from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django_faculdade_site.apps.cad_roupas.models import User


# Create your views here.

@login_required(login_url="/accounts/login/")
def add_user(req):
    add_user_form = AddUserForm()

    return render(
        request=req,
        template_name="perfil/perfil.html",
        context={
            "form": add_user_form
        }
    )
