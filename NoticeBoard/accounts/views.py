from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        # Basic validation
        if not (username and password and password == confirm_password):
            return render(request, 'auth/register.html', {'error': 'Invalid input'})

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', {'error': 'Username is already taken'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'auth/register.html', {'error': 'Email is already in use'})
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        # Log in the user
        login(request, user)
        return redirect('notices_home')  # Redirect to the home page after successful registration

    return render(request, 'auth/register.html')
