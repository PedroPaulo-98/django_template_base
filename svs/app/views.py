from django.shortcuts import render

# Create your views here.
from django.db.models import Sum
from django.utils import timezone
from django.http import JsonResponse
from .models import Quantity_hospital
from collections import defaultdict

def get_hospitalizations_by_month(request):
    # Filtra os dados do último ano (ou ajuste conforme necessário)
    one_year_ago = timezone.now() - timezone.timedelta(days=365)
    hospitalizations = Quantity_hospital.objects.filter(insert_in__gte=one_year_ago)

    # Agrupa os dados por mês
    monthly_data = defaultdict(lambda: {
        'total': 0,
        'categories': {
            't0_to_28_days_male': 0,
            't0_to_28_days_female': 0,
            't29d_to_1y_male': 0,
            't29d_to_1y_female': 0,
            't1y_to_5y_male': 0,
            't1y_to_5y_female': 0,
            't6y_to_10y_male': 0,
            't6y_to_10y_female': 0,
            't11y_to_17y_male': 0,
            't11y_to_17y_female': 0,
            'adult_male': 0,
            'adult_female': 0,
            'old_male': 0,
            'old_female': 0,
        }
    })

    for entry in hospitalizations:
        month_year = entry.insert_in.strftime('%Y-%m')  # Agrupa por mês e ano
        for field in monthly_data[month_year]['categories']:
            monthly_data[month_year]['categories'][field] += getattr(entry, field)
        monthly_data[month_year]['total'] += sum(getattr(entry, field) for field in monthly_data[month_year]['categories'])

    # Prepara os dados para o gráfico
    labels = sorted(monthly_data.keys())
    totals = [monthly_data[month]['total'] for month in labels]
    categories = {
        't0_to_28_days': [monthly_data[month]['categories']['t0_to_28_days_male'] + monthly_data[month]['categories']['t0_to_28_days_female'] for month in labels],
        't29d_to_1y': [monthly_data[month]['categories']['t29d_to_1y_male'] + monthly_data[month]['categories']['t29d_to_1y_female'] for month in labels],
        't1y_to_5y': [monthly_data[month]['categories']['t1y_to_5y_male'] + monthly_data[month]['categories']['t1y_to_5y_female'] for month in labels],
        't6y_to_10y': [monthly_data[month]['categories']['t6y_to_10y_male'] + monthly_data[month]['categories']['t6y_to_10y_female'] for month in labels],
        't11y_to_17y': [monthly_data[month]['categories']['t11y_to_17y_male'] + monthly_data[month]['categories']['t11y_to_17y_female'] for month in labels],
        'adult': [monthly_data[month]['categories']['adult_male'] + monthly_data[month]['categories']['adult_female'] for month in labels],
        'old': [monthly_data[month]['categories']['old_male'] + monthly_data[month]['categories']['old_female'] for month in labels],
    }

    return JsonResponse({
        'labels': labels,
        'totals': totals,
        'categories': categories,
    })