from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Issue, Category
from django.contrib import messages

from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

@login_required
def raise_issue(request):
	categories = Category.objects.all()

	if request.method == 'POST':
		title = request.POST.get('title')
		description = request.POST.get('description')
		location = request.POST.get('location')
		category_id = request.POST.get('category')

		category = Category.objects.get(id=category_id)

		Issue.objects.create(
			title=title,
			description=description,
			location=location,
			category=category,
			created_by = request.user
		)

		messages.success(request,"Issue raised succesfully")
		return redirect('/dashboard/citizen/')
	
	return render(request,'issues/raise_issue.html',{'categories': categories})

@login_required
def issue_list(request):
    issues = Issue.objects.select_related('category', 'created_by') \
        .order_by('-category__is_emergency', '-created_at')

    return render(request, 'issues/issue_list.html', {'issues': issues})

@login_required
def update_issue_status(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)

    # Permission check
    if not (request.user.is_superuser or request.user.profile.role >= 2):
        return HttpResponseForbidden("You are not allowed to update this issue")

    if request.method == 'POST':
        status = request.POST.get('status')
        remarks = request.POST.get('remarks')

        issue.status = status
        issue.remarks = remarks
        issue.assigned_to = request.user
        issue.save()

        messages.success(request, "Issue updated successfully")
        return redirect('issue_list')

    return render(request, 'issues/update_issue.html', {'issue': issue})

@login_required
def assign_issue(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)

    # 🔐 Admin-only check
    if not (request.user.is_superuser or request.user.profile.role == 3):
        return HttpResponseForbidden("Only admin can assign issues")

    staff_users = User.objects.filter(profile__role__gte=2)

    if request.method == 'POST':
        staff_id = request.POST.get('staff')
        staff_user = User.objects.get(id=staff_id)

        issue.assigned_to = staff_user
        issue.save()

        messages.success(request, "Issue assigned successfully")
        return redirect('issue_list')

    return render(
        request,
        'issues/assign_issue.html',
        {
            'issue': issue,
            'staff_users': staff_users
        }
    )
