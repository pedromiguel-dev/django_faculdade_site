from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.entrega, name="entrega"),
    path(route="info/", view=views.entrega_info, name="entrega_info"),
    path(route="reg/", view=views.entrega_reg, name="registrar_entrega"),
]