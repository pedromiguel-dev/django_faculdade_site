from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.carrinho, name="carrinho"),
    path(route="render_cards/", view=views.carrinho_cards, name="carrinho_cards"),
    path(route="render_info/", view=views.carrinho_info, name="carrinho_info"),
    path(route="add/<id_roupa>/", view=views.carrinho_add, name="add_carrinho"),
    path(route="del/<id_roupa>/", view=views.carrinho_del, name="deletar_carrinho"),
]