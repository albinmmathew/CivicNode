from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from issues.models import Issue

@login_required
def citizen_dashboard(request):
    user_issues = Issue.objects.filter(created_by=request.user)
    
    stats = {
        'total': user_issues.count(),
        'pending': user_issues.filter(status='PENDING').count(),
        'in_progress': user_issues.filter(status='IN_PROGRESS').count(),
        'resolved': user_issues.filter(status='RESOLVED').count(),
    }
    
    recent_issues = user_issues.order_by('-created_at')[:5]
    
    return render(request, 'dashboard/citizen_dashboard.html', {
        'stats': stats,
        'recent_issues': recent_issues
    })

@login_required
def staff_dashboard(request):
    # Staff/Admin can see issues assigned to them or all issues if superuser
    if request.user.is_superuser:
        relevant_issues = Issue.objects.all()
    else:
        relevant_issues = Issue.objects.filter(assigned_to=request.user)
        
    stats = {
        'total': relevant_issues.count(),
        'pending': relevant_issues.filter(status='PENDING').count(),
        'in_progress': relevant_issues.filter(status='IN_PROGRESS').count(),
        'resolved': relevant_issues.filter(status='RESOLVED').count(),
    }
    
    # Global stats for staff overview
    all_issues = Issue.objects.all()
    global_stats = {
        'critical': all_issues.filter(category__is_emergency=True, status__in=['PENDING', 'IN_PROGRESS']).count(),
        'unassigned': all_issues.filter(assigned_to__isnull=True).count(),
    }
    
    return render(request, 'dashboard/staff_dashboard.html', {
        'stats': stats,
        'global_stats': global_stats,
        'relevant_issues': relevant_issues.order_by('-created_at')[:10]
    })
