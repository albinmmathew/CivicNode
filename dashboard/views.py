from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def citizen_dashboard(request):
    role = request.user.profile.role
    return render(request, 'dashboard/citizen_dashboard.html', {'role': role})

@login_required
def staff_dashboard(request):
    role = request.user.profile.role
    return render(request, 'dashboard/staff_dashboard.html', {'role': role})
