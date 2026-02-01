from django.urls import path
from . import views

urlpatterns = [
    path('', views.citizen_dashboard,name='citizen_dashboard'),
    path('staff/', views.staff_dashboard),
]
