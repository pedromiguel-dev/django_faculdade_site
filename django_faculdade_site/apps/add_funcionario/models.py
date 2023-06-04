from django.contrib.auth.base_user import BaseUserManager
from django.db import models

from django_faculdade_site.apps.accounts.models import User


# Create your models here.


class FuncionarioManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.FUNCIONARIO)


class Funcionario(User):
    base_role = User.Role.FUNCIONARIO

    funcionario = FuncionarioManager()

    class Meta:
        proxy = True

