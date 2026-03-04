from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def landing(request):
    if request.user.is_authenticated:
        if request.user.profile.role >= 2:
            return redirect('assigned_issues')
        return redirect('dashboard')
    return render(request, 'dashboard/landing.html')

@login_required
def dashboard(request):
    role = request.user.profile.role
    return render(request, 'dashboard/dashboard.html', {'role': role})
