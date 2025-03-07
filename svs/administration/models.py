from django.db import models
from administration.manager import CustomUserManager
from django.contrib.auth.models import Group, Permission, AbstractUser
from django.core.validators import RegexValidator



class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=14, 
        unique=True, 
        validators=[RegexValidator(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', message="CPF inválido. Formato esperado: 000.000.000-00")]
    )
    photo = models.ImageField(upload_to='documentos/', null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set",  # Nome único para evitar conflitos
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",  # Nome único para evitar conflitos
        related_query_name="user",
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["username", "email"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
