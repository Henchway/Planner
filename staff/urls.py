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

from staff.views import StaffListView, StaffDetailView, StaffDeleteView, StaffCreateView, StaffUpdateView

app_name = 'staff'
urlpatterns = [
    path('', StaffListView.as_view(), name='staff-list'),
    path('create/', StaffCreateView.as_view(), name='staff-create'),
    path('<int:id>/', StaffDetailView.as_view(), name='staff-detail'),
    path('<int:id>/update/', StaffUpdateView.as_view(), name='staff-update'),
    path('<int:id>/delete/', StaffDeleteView.as_view(), name='staff-delete'),
]
