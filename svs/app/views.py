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
        month_year = entry.insert_in.strftime('%m-%Y')  # Agrupa por mês e ano
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


def get_hospitalizations_by_sex(request):
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
        month_year = entry.insert_in.strftime('%m-%Y')  # Agrupa por mês e ano
        for field in monthly_data[month_year]['categories']:
            monthly_data[month_year]['categories'][field] += getattr(entry, field)
        monthly_data[month_year]['total'] += sum(getattr(entry, field) for field in monthly_data[month_year]['categories'])

    # Prepara os dados para o gráfico
    labels = sorted(monthly_data.keys())
    totals = [monthly_data[month]['total'] for month in labels]
    categories = {
        'Male': [monthly_data[month]['categories']['t0_to_28_days_male'] + monthly_data[month]['categories']['t29d_to_1y_male'] + monthly_data[month]['categories']['t1y_to_5y_male'] + monthly_data[month]['categories']['t6y_to_10y_male'] + monthly_data[month]['categories']['t11y_to_17y_male'] + monthly_data[month]['categories']['adult_male'] + monthly_data[month]['categories']['old_male'] for month in labels],
        'Female': [monthly_data[month]['categories']['t0_to_28_days_female'] + monthly_data[month]['categories']['t29d_to_1y_female'] + monthly_data[month]['categories']['t1y_to_5y_female'] + monthly_data[month]['categories']['t6y_to_10y_female'] + monthly_data[month]['categories']['t11y_to_17y_female'] + monthly_data[month]['categories']['adult_female'] + monthly_data[month]['categories']['old_female'] for month in labels],
    }

    return JsonResponse({
        'labels': labels,
        'totals': totals,
        'categories': categories,
    })


def get_hospitalizations_by_day(request):
    # Filtra os dados do último ano (ou ajuste conforme necessário)
    one_year_ago = timezone.now() - timezone.timedelta(days=365)
    hospitalizations = Quantity_hospital.objects.filter(insert_in__gte=one_year_ago)

    # Agrupa os dados por mês
    dayly_data = defaultdict(lambda: {
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
        day_year = entry.insert_in.strftime('%d-%m-%y')  # Agrupa por mês e ano
        for field in dayly_data[day_year]['categories']:
            dayly_data[day_year]['categories'][field] += getattr(entry, field)
        dayly_data[day_year]['total'] += sum(getattr(entry, field) for field in dayly_data[day_year]['categories'])

    # Prepara os dados para o gráfico
    labels = sorted(dayly_data.keys())
    totals = [dayly_data[day]['total'] for day in labels]
    categories = {
        't0_to_28_days': [dayly_data[day]['categories']['t0_to_28_days_male'] + dayly_data[day]['categories']['t0_to_28_days_female'] for day in labels],
        't29d_to_1y': [dayly_data[day]['categories']['t29d_to_1y_male'] + dayly_data[day]['categories']['t29d_to_1y_female'] for day in labels],
        't1y_to_5y': [dayly_data[day]['categories']['t1y_to_5y_male'] + dayly_data[day]['categories']['t1y_to_5y_female'] for day in labels],
        't6y_to_10y': [dayly_data[day]['categories']['t6y_to_10y_male'] + dayly_data[day]['categories']['t6y_to_10y_female'] for day in labels],
        't11y_to_17y': [dayly_data[day]['categories']['t11y_to_17y_male'] + dayly_data[day]['categories']['t11y_to_17y_female'] for day in labels],
        'adult': [dayly_data[day]['categories']['adult_male'] + dayly_data[day]['categories']['adult_female'] for day in labels],
        'old': [dayly_data[day]['categories']['old_male'] + dayly_data[day]['categories']['old_female'] for day in labels],
    }

    return JsonResponse({
        'labels': labels,
        'totals': totals,
        'categories': categories,
    })


def get_hospitalizations_by_day_sex(request):
    # Filtra os dados do último ano (ou ajuste conforme necessário)
    one_year_ago = timezone.now() - timezone.timedelta(days=365)
    hospitalizations = Quantity_hospital.objects.filter(insert_in__gte=one_year_ago)

    # Agrupa os dados por dia
    daily_data = defaultdict(lambda: {
        'total': 0,
        'categories': {
            'male': 0,
            'female': 0,
        }
    })

    for entry in hospitalizations:
        day_year = entry.insert_in.strftime('%d-%m-%Y')  # Agrupa por dia, mês e ano
        daily_data[day_year]['categories']['male'] += entry.t0_to_28_days_male + entry.t29d_to_1y_male + entry.t1y_to_5y_male + entry.t6y_to_10y_male + entry.t11y_to_17y_male + entry.old_male
        daily_data[day_year]['categories']['female'] += entry.t0_to_28_days_female + entry.t29d_to_1y_female + entry.t1y_to_5y_female + entry.t6y_to_10y_female + entry.t11y_to_17y_female + entry.old_female
        daily_data[day_year]['total'] += sum([
            entry.t0_to_28_days_male, entry.t0_to_28_days_female,
            entry.t29d_to_1y_male, entry.t29d_to_1y_female,
            entry.t1y_to_5y_male, entry.t1y_to_5y_female,
            entry.t6y_to_10y_male, entry.t6y_to_10y_female,
            entry.t11y_to_17y_male, entry.t11y_to_17y_female,
            entry.adult_male, entry.adult_female,
            entry.old_male, entry.old_female,
        ])

    # Prepara os dados para o gráfico
    labels = sorted(daily_data.keys())
    totals = [daily_data[day]['total'] for day in labels]
    categories = {
        'male': [daily_data[day]['categories']['male'] for day in labels],
        'female': [daily_data[day]['categories']['female'] for day in labels],
    }

    return JsonResponse({
        'labels': labels,
        'totals': totals,
        'categories': categories,
    })


def get_hospitalizations_by_day2(request):
    # Filtra os dados do último ano (ou ajuste conforme necessário)
    one_year_ago = timezone.now() - timezone.timedelta(days=365)
    hospitalizations = Quantity_hospital.objects.filter(insert_in__gte=one_year_ago)

    # Agrupa os dados por dia
    daily_data = defaultdict(lambda: {
        'total': 0,
        'categories': {
            't0_to_28_days': 0,
            't29d_to_1y': 0,
            't1y_to_5y': 0,
            't6y_to_10y': 0,
            't11y_to_17y': 0,
            'adult': 0,
            'old': 0,
        }
    })

    for entry in hospitalizations:
        day_year = entry.insert_in.strftime('%d-%m-%Y')  # Agrupa por dia, mês e ano
        daily_data[day_year]['categories']['t0_to_28_days'] += entry.t0_to_28_days_male + entry.t0_to_28_days_female
        daily_data[day_year]['categories']['t29d_to_1y'] += entry.t29d_to_1y_male + entry.t29d_to_1y_female
        daily_data[day_year]['categories']['t1y_to_5y'] += entry.t1y_to_5y_male + entry.t1y_to_5y_female
        daily_data[day_year]['categories']['t6y_to_10y'] += entry.t6y_to_10y_male + entry.t6y_to_10y_female
        daily_data[day_year]['categories']['t11y_to_17y'] += entry.t11y_to_17y_male + entry.t11y_to_17y_female
        daily_data[day_year]['categories']['adult'] += entry.adult_male + entry.adult_female
        daily_data[day_year]['categories']['old'] += entry.old_male + entry.old_female
        daily_data[day_year]['total'] += sum([
            entry.t0_to_28_days_male, entry.t0_to_28_days_female,
            entry.t29d_to_1y_male, entry.t29d_to_1y_female,
            entry.t1y_to_5y_male, entry.t1y_to_5y_female,
            entry.t6y_to_10y_male, entry.t6y_to_10y_female,
            entry.t11y_to_17y_male, entry.t11y_to_17y_female,
            entry.adult_male, entry.adult_female,
            entry.old_male, entry.old_female,
        ])

    # Prepara os dados para o gráfico
    labels = sorted(daily_data.keys())
    totals = [daily_data[day]['total'] for day in labels]
    categories = {
        't0_to_28_days': [daily_data[day]['categories']['t0_to_28_days'] for day in labels],
        't29d_to_1y': [daily_data[day]['categories']['t29d_to_1y'] for day in labels],
        't1y_to_5y': [daily_data[day]['categories']['t1y_to_5y'] for day in labels],
        't6y_to_10y': [daily_data[day]['categories']['t6y_to_10y'] for day in labels],
        't11y_to_17y': [daily_data[day]['categories']['t11y_to_17y'] for day in labels],
        'adult': [daily_data[day]['categories']['adult'] for day in labels],
        'old': [daily_data[day]['categories']['old'] for day in labels],
    }

    return JsonResponse({
        'labels': labels,
        'totals': totals,
        'categories': categories,
    })