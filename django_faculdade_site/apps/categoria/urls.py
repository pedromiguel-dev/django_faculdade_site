from django.urls import path
from . import views

urlpatterns = [
    path(route="reach/<cat>/", view=views.categoria, name="categoria"),
    path(route="cards", view=views.categorias_cards, name="categoria_card"),
]