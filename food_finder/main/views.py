from django.shortcuts import render

# Create your views here.
def returnHomePage(request):
    return render(request, 'main/home.html', {'isLoggedIn': False})