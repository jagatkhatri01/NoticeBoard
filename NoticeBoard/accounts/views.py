from django.shortcuts import render, redirect   
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')

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
        return redirect('notices')  # Redirect to the home page after successful registration

    return render(request, 'auth/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('notices')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid Input'})
    return render(request, 'auth/login.html')


@login_required
def demo(request):
    return HttpResponse('This is index page')

