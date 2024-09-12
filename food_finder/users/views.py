from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def signUpUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('/')  # Replace 'home' with your desired URL
    else:
        form = UserCreationForm()
    
    return render(request, 'users/signup.html', {'form': form})