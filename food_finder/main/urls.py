from django.urls import path
from .views import returnHomePage

urlpatterns = [
    path('', returnHomePage, name='home'),
    # ... other url patterns
]