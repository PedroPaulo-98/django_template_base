from django.contrib import admin
from .models import City, Hospital, Illnesses, Epidemiological_weeks, Hospitalization_Information, Quantity_hospital
from django.contrib.admin import ModelAdmin, TabularInline, register


class quantidade_hospitalsInLine(TabularInline):
    model = Quantity_hospital
    extra = 1
    readonly_fields = ['insert_in']


# Register your models here.

from django.contrib.admin import ModelAdmin, TabularInline, register

@register(City)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'local_hospital'

@register(Hospital)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'local_hospital'

@register(Illnesses)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'local_hospital'

@register(Epidemiological_weeks)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'local_hospital'

@register(Hospitalization_Information)
class VacinometroAdmin(ModelAdmin): # type: ignore
    icon_name = 'local_hospital'
    extra = 1
    inlines = [quantidade_hospitalsInLine]
