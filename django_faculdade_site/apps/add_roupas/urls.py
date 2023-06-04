from django.urls import path
from .views import register_roupa, register_categoria, edit_roupa, rem_roupa

urlpatterns = [
    path("roupa/", register_roupa, name="funcionario" ),
    path("roupa/<id_roupa>", edit_roupa, name="edit_roupa" ),
    path("rem_roupa/<id_roupa>", rem_roupa, name="rem_roupa" ),
    path("categoria/", register_categoria, name="categoria_admin"),
]