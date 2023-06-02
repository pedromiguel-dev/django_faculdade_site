from django_faculdade_site.apps.cad_roupas.models import Funcionario
from django import forms


class AddUserForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        attrs = {'class': 'form-control'}
        fields = ['username', 'email', 'password1', 'password2']
