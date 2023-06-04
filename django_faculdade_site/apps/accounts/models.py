from datetime import datetime, timedelta

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


def utc_ten_days_future():
    return datetime.utcnow() + timedelta(days=10)


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        FUNCIONARIO = "FUNCIONARIO", 'Funcionário'
        CLIENTE = "CLIENTE", 'Client'

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class ClienteManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENTE)


class Cliente(User):
    base_role = User.Role.CLIENTE

    cliente = ClienteManager()

    class Meta:
        proxy = True
