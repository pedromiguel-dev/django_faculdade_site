from django.urls import path
from django.conf import settings #add this
from django.conf.urls.static import static #add this
from .views import sign_up, sign_in

urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("signin/", sign_in, name="signin"),
]