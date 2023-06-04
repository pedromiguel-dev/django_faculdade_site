from django.contrib.auth.forms import UserCreationForm

from django import forms

from django_faculdade_site.apps.add_funcionario.models import Funcionario


class AddUserForm(UserCreationForm):
    class Meta:
        model = Funcionario
        attrs = {'class': 'form-control'}
        fields = ['username', 'email', 'password1', 'password2']