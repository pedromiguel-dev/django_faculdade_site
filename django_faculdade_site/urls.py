from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django_faculdade_site.apps.home.views import home
from django_faculdade_site.apps.roupa.views import roupa
from django_faculdade_site.apps.entrega.views import agradecimento
from django_faculdade_site.apps.perfil.views import perfil

urlpatterns = [
    path(route="", view=home),
    path(route="", view=include("django_faculdade_site.apps.accounts.urls")),
    path(route="adm/", view=include("django_faculdade_site.apps.add_funcionario.urls")),
    path(route="funcionario/", view=include("django_faculdade_site.apps.add_roupas.urls")),
    path(route="carrinho/", view=include("django_faculdade_site.apps.carrinho.urls")),
    path(route="entrega/", view=include("django_faculdade_site.apps.entrega.urls")),
    path(route="categoria/", view=include("django_faculdade_site.apps.categoria.urls")),

    path(route="agradecimento/", view=agradecimento),
    path(route="accounts/profile/", view=perfil, name="perfil"),
    path(route="roupa/<id_roupa>/", view=roupa, name="roupa"),
]

url_django = [
    path(route="admin/", view=admin.site.urls),
    path(route="accounts/", view=include("django.contrib.auth.urls")),
]

urlpatterns += url_django

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
