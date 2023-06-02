from django.contrib.auth.forms import UserCreationForm

from django_faculdade_site.apps.cad_roupas.models import Funcionario, Roupa
from django import forms


class AddUserForm(UserCreationForm):
    class Meta:
        model = Funcionario
        attrs = {'class': 'form-control'}
        fields = ['username', 'email', 'password1', 'password2']