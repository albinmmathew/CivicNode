from django.shortcuts import render ,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login  as auth_login

# For registering user
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Checking for blank entries
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required")
            return redirect('register')
        
		# Ensuring password matches
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

		# Ensuring Unique User
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        
		# Ensuring one User per Email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

		# Creating User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'accounts/register.html')

#for logging in registered users to respective dashboards
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

			# if user is supperuser then redirects to admin page
            if user.is_superuser:
                return redirect('/admin/')

            role = user.profile.role

            if role == 3:
                return redirect('/admin/')
            elif role == 2:
                return redirect('/dashboard/staff/')
            else:
                return redirect('/dashboard/citizen/')

        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'accounts/login.html')
