from django.urls import path
from . import views

urlpatterns =[
	path('raise/',views.raise_issue,name='raise_issue'),
    path('', views.issue_list, name='issue_list'),
]