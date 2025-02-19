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
from django.shortcuts import render
from app.views import get_hospitalizations_by_month


def user_settings_view(request):
    return render(request, 'admin/user.html')
def dashboard_view(request):
    return render(request, 'admin/dashboard.html')

urlpatterns = [
    path('user/', user_settings_view, name='user-settings'),
    path('dashboard/', dashboard_view, name='dashboard'),
     path('api/hospitalizations-by-month/', get_hospitalizations_by_month, name='hospitalizations_by_month'),
    path('', admin.site.urls),
]
