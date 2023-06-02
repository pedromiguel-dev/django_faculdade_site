from django.urls import path
from django.conf import settings #add this
from django.conf.urls.static import static #add this
from .views import sign_up, sign_in, register_roupa, register_categoria

urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("signin/", sign_in, name="signin"),
    path("funcionario/", register_roupa, name="funcionario" ),
    path("categoria-admin/", register_categoria, name="categoria_admin"),
]

if settings.DEBUG: #add this
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
