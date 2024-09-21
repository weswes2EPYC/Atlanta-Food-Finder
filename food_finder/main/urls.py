from django.urls import path
from .views import returnHomePage, restaurantDetailsPage

urlpatterns = [
    path('', returnHomePage, name='home'),
    path('restaurant/<int:restaurant_id>/', restaurantDetailsPage, name='details')
    # ... other url patterns
]