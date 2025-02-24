"""
URL configuration for svs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.shortcuts import render
from app.views import get_hospitalizations_by_month, get_hospitalizations_by_sex, get_hospitalizations_by_day, get_hospitalizations_by_day2, get_hospitalizations_by_day_sex


def user_settings_view(request):
    return render(request, 'admin/user.html')
def dashboard_view(request):
    return render(request, 'admin/dashboard.html')
def dashboardday_view(request):
    return render(request, 'admin/dashboardday.html')
def dashboardmouth_view(request):
    return render(request, 'admin/dashboradmouth.html')


urlpatterns = [
    path('user/', user_settings_view, name='user-settings'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboardday/', dashboardday_view, name='dashboardday'),
    path('dashboardmouth/', dashboardmouth_view, name='dashboardmouth'),
    path('api/hospitalizations-by-month/', get_hospitalizations_by_month, name='hospitalizations_by_month'),
    path('api/hospitalizations_by_sex/', get_hospitalizations_by_sex, name='hospitalizations_by_sex'),
    path('api/hospitalizations_by_day/', get_hospitalizations_by_day, name='hospitalizations_by_day'),
    path('api/hospitalizations_by_day2/', get_hospitalizations_by_day2, name='hospitalizations_by_day2'),
    path('api/get_hospitalizations_by_day_sex/', get_hospitalizations_by_day_sex, name='hospitalizations_by_day_sex'),
    path('', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
