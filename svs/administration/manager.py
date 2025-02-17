from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, cpf, password=None, **extra_fields):
        if not cpf:
            raise ValueError('The cpf field must be set')
        cpf = self.normalize_email(cpf)
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(cpf, password, **extra_fields)

