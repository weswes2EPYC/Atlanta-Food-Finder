from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def signUpUser(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Handle error states
        if not username or not password:
            return render(request, "users/signup.html", {'error': 'Please fill in all fields'})
        
        if len(password) < 8:
            return render(request, "users/signup.html", {'error': 'Password must be at least 8 characters long'})
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "users/signup.html", {'error': 'Account with the username already exists'})
        
        # Passed error checks, so we create a new user and login user
        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.save()

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("/")
    
    # If not a post, just return empty form
    return render(request, 'users/signup.html')


def signInUser(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Handle error states
        if not username or not password:
            return render(request, "users/signin.html", {'error': 'Please fill in all fields'})
        
        # Passed error checks, so login user
        user = authenticate(username=username, password=password)
        if (not user):
            return render(request, 'users/signin.html', {'error': 'Wrong user credentials'})
        login(request, user)

        return redirect("/")
    
    # If not a post, just return empty form
    return render(request, 'users/signin.html')

def logoutUser(request):
    logout(request)
    request.session.clear()
    return redirect("/")