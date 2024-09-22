from django.urls import path
from .views import returnHomePage, restaurantDetailsPage, saveRestaurant

urlpatterns = [
    path('', returnHomePage, name='home'),
    path('restaurant/<int:restaurant_id>/', restaurantDetailsPage, name='details'),
    path('save/<str:restaurant_id>/', saveRestaurant, name='save')
    # ... other url patterns
]