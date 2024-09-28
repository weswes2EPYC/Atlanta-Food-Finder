from django.urls import path
from .views import returnHomePage, restaurantDetailsPage, saveRestaurant, favoritesPage
from . import views
urlpatterns = [
    path('', returnHomePage, name='home'),
    path('restaurants/', views.restaurants_view, name='restaurants'),
    path('restaurants.html', views.restaurants_view, name='restaurants'),
    path('restaurant/<str:restaurant_id>/', restaurantDetailsPage, name='details'),
    path('save/<str:restaurant_id>/', saveRestaurant, name='save'),
    path('saved', favoritesPage, name="saved")
    # ... other url patterns
]