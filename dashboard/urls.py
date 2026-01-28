from django.urls import path
from . import views

urlpatterns = [
    path('citizen/', views.citizen_dashboard),
    path('staff/', views.staff_dashboard),
]
