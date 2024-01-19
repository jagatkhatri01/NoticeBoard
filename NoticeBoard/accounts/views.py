from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')

        if not (username and password and password == confirm_password):
            return render(request, 'auth/register.html', {'error': 'Invalid input'})

        if User.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', {'error': 'Username is already taken'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'auth/register.html', {'error': 'Email is already in use'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration successful. Please log in.')
        return redirect('login')  
    
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

def logout_view(request):
    logout(request)
    return redirect('notices')


@login_required
def demo(request):
    return HttpResponse('This is index page')

