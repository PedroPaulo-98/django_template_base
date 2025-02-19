from django.contrib import admin
from .models import City, Hospital, Illnesses, Epidemiological_weeks, Hospitalization_Information, Quantity_hospital
from django.contrib.admin import ModelAdmin, TabularInline, register
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model



#User = get_user_model()
#
#class CustomUserAdmin(UserAdmin):
#    # Adiciona o campo 'cpf' ao formulário de edição de usuário
#    fieldsets = UserAdmin.fieldsets + (
#        ('Informações Adicionais', {'fields': ('cpf',)}),
#    )
#    
#    # Adiciona o campo 'cpf' ao formulário de criação de usuário
#    add_fieldsets = UserAdmin.add_fieldsets + (
#        ('Informações Adicionais', {'fields': ('cpf',)}),
#    )
#    
#    # Exibe o campo 'cpf' na lista de usuários no admin
#    list_display = ('username', 'email', 'cpf', 'is_staff')
#
## Registra o modelo User personalizado
#admin.site.register(User, CustomUserAdmin)




class quantidade_hospitalsInLine(TabularInline):
    model = Quantity_hospital
    extra = 1
    readonly_fields = ['insert_in']


# Register your models here.

from django.contrib.admin import ModelAdmin, TabularInline, register

@register(City)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'local_hospital'
    actions = None

@register(Hospital)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'local_hospital'
    actions = None

@register(Illnesses)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'local_hospital'
    actions = None

@register(Epidemiological_weeks)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'local_hospital'
    actions = None

@register(Hospitalization_Information)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'local_hospital'
    extra = 1
    inlines = [quantidade_hospitalsInLine]
    actions = None
