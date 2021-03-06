"""Planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from apps.pages.views import home_view

admin.autodiscover()

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('staff/', include('apps.staff.urls')),
    path('shift/', include('apps.shift.urls')),
    path('schedule/', include('apps.schedule.urls')),
    path('day/', include('apps.day.urls')),
    path('location/', include('apps.location.urls')),
]
