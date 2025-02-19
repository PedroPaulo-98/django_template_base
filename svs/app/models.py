from django.db import models
from django.contrib.auth.models import User # type: ignore
from django.utils.translation import gettext as _t, gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

#class User(AbstractUser):
#    cpf = models.CharField(
#        max_length=14, 
#        unique=True, 
#        validators=[RegexValidator(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', message="CPF inválido. Formato esperado: 000.000.000-00")]
#    )
#
#    # Adicione related_name únicos para evitar conflitos
#    groups = models.ManyToManyField(
#        Group,
#        verbose_name='groups',
#        blank=True,
#        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#        related_name="custom_user_set",  # Nome único para evitar conflitos
#        related_query_name="user",
#    )
#    user_permissions = models.ManyToManyField(
#        Permission,
#        verbose_name='user permissions',
#        blank=True,
#        help_text='Specific permissions for this user.',
#        related_name="custom_user_set",  # Nome único para evitar conflitos
#        related_query_name="user",
#    )
#
#    def __str__(self):
#        return self.username
#
##Validação de Data
#def validate_future_date(value):
#    if value.year < 2023:
#        raise ValidationError('A data não pode ser no passado.')
    

#------------------------------------------------------------------------------------------------------
    
# Cidades
class City (models.Model):
    city = models.CharField("Cidade",max_length=150)
    state = models.CharField("Estado",max_length=150)

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


#------------------------------------------------------------------------------------------------------

# Hospital
class Hospital (models.Model):
    name = models.CharField("Nome do Hospital",max_length=150)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Cidade")
    specialty = models.CharField("Especialidade do Hospital",max_length=150)
    location = models.CharField("Localização do Hospital",max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "hospital"
        verbose_name_plural = "hospitais"


#------------------------------------------------------------------------------------------------------

#Doenças
class Illnesses (models.Model):

    PRIORIDADE_CHOICES = (
        (0, "Baixa"),
        (1, "Média"),
        (2, "Alta")
    )
        
    name = models.CharField("Nome da Doença",max_length=150)
    degree_risk = models.IntegerField("Grau de risco", choices=PRIORIDADE_CHOICES,default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Doença"
        verbose_name_plural = "Doenças"


#------------------------------------------------------------------------------------------------------

#semana epidemiologica
class Epidemiological_weeks (models.Model):
        
    se = models.CharField("SE (semana epidemiologica)",max_length=150)
    year = models.IntegerField("ano")

    def __str__(self):
        return self.se
    
    class Meta:
        verbose_name = "Semana Epidemiologicas"
        verbose_name_plural = "Semana Epidemiologicas"


#------------------------------------------------------------------------------------------------------

#Informações de Internações 
class Hospitalization_Information (models.Model):
    info = models.CharField("dados das internações",max_length=150, null=True, blank=True,)
    date = models.DateField("Data", default=timezone.now)
    se = models.ForeignKey(Epidemiological_weeks, on_delete=models.CASCADE, verbose_name="SE")
    illnesses = models.ForeignKey(Illnesses, on_delete=models.CASCADE, verbose_name="Doença")


    def __str__(self):
        return self.info
    
    class Meta:
        verbose_name = "Internações por dia"
        verbose_name_plural = "Internações por dia"


#------------------------------------------------------------------------------------------------------

#Quandtidade por hospital
class Quantity_hospital (models.Model):

    CHOICES = (
        ("Clinica", "Clinica"),
        ("UTI", "UTI")
    )


    internacao_id = models.ForeignKey(Hospitalization_Information, on_delete=models.CASCADE, verbose_name="internação")
    insert_in = models.DateTimeField(_("Inserido em"), default=timezone.now)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name="Hospital")
    clinic_UTI = models.CharField("Tipo de internação", choices=CHOICES,default=0, max_length=150)
    t0_to_28_days_male = models.IntegerField("Homem de 0 a 28 dias", default=0)
    t0_to_28_days_female = models.IntegerField("Mulher de 0 a 28 dias", default=0)
    t29d_to_1y_male = models.IntegerField("Homem de 29 dias a 1 ano", default=0)
    t29d_to_1y_female = models.IntegerField("Mulher de 29 dias a 1 ano", default=0)
    t1y_to_5y_male = models.IntegerField("Homem de 1 a 5 anos", default=0)
    t1y_to_5y_female = models.IntegerField("Mulher de 1 a 5 anos", default=0)
    t6y_to_10y_male = models.IntegerField("Homem de 6 a 10 anos", default=0)
    t6y_to_10y_female = models.IntegerField("Mulher de 6 a 10 anos", default=0)
    t11y_to_17y_male = models.IntegerField("Homem de 11 a 17 anos", default=0)
    t11y_to_17y_female = models.IntegerField("Mulher de 11 a 17 anos", default=0)
    adult_male = models.IntegerField("Homem Adulto", default=0)
    adult_female = models.IntegerField("Mulher Adulta", default=0)
    old_male = models.IntegerField("Homem Idoso", default=0)
    old_female = models.IntegerField("Mulher Idosa", default=0)

    #def __date__(self):
    #    return self.internacao_id
    
    class Meta:
        verbose_name = "Quantidade por hospital"
        verbose_name_plural = "Quantidade por hospitais"