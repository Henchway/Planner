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

from django.urls import path

from .views import ShiftListView, ShiftDetailView, ShiftCreateView, ShiftUpdateView, ShiftDeleteView

app_name = 'shift'
urlpatterns = [
    path('', ShiftListView.as_view(), name='shift-list'),
    path('<int:id>/', ShiftDetailView.as_view(), name='shift-detail'),
    path('create/', ShiftCreateView.as_view(), name='shift-create'),
    path('<int:id>/update/', ShiftUpdateView.as_view(), name='shift-update'),
    path('<int:id>/delete/', ShiftDeleteView.as_view(), name='shift-delete'),
]
