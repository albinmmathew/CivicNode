from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Issue, Category
from django.contrib import messages

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
	
	return render(request,'issues/raise_issue.html'),{'categories': categories}