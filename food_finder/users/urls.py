from django.urls import path
from .views import signUpUser

urlpatterns = [
    path('signup/', signUpUser, name='signup'),
    # ... other url patterns
]