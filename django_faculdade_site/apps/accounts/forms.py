from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django_faculdade_site.apps.cad_roupas.models import Cliente, User, Roupa, Categoria


class RegisterForm(UserCreationForm):
    class Meta:
        model = Cliente
        attrs = {'class': 'form-control'}
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        attrs = {'class': 'form-control'}
        fields = ['email', 'password']


class RegisterRoupa(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome', 'descricao', 'valor', 'precoLavagem', 'categoria', 'imagem']


class EditRoupa(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome', 'descricao', 'valor', 'precoLavagem', 'categoria', 'imagem']


class RegisterCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao', 'imagem']
