from django.urls import path

from django_faculdade_site.apps.add_funcionario.views import add_user, rem_user

urlpatterns = [
    path(route="add_funcionario/", view=add_user, name="add_funcionario"),
    path(route="rem_funcionario/<id_user>/", view=rem_user, name="rem_funcionario"),
]