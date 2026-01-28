from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def citizen_dashboard(request):
    return render(request, 'dashboard/citizen_dashboard.html')

@login_required
def staff_dashboard(request):
    return HttpResponse("Staff Dashboard")
