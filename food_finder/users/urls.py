from django.urls import path
from .views import signUpUser, signInUser, logoutUser

urlpatterns = [
    path('signup/', signUpUser, name='signup'),
    path('signin/', signInUser, name='signin'),
    path('logout/', logoutUser, name='logout'),
    # ... other url patterns
]