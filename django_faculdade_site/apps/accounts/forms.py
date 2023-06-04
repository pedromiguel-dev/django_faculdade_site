from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from django_faculdade_site.apps.accounts.models import Cliente, User


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