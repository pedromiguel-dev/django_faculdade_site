from django import forms

from django_faculdade_site.apps.categoria.models import Categoria
from django_faculdade_site.apps.roupa.models import Roupa


class RegisterRoupa(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome', 'descricao', 'valor', 'precoLavagem', 'categoria', 'imagem', 'quantidade']


class EditRoupa(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome', 'descricao', 'valor', 'precoLavagem', 'categoria', 'imagem', 'quantidade']


class RegisterCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao', 'imagem']
