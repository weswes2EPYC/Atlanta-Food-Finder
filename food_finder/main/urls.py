from django.urls import path
from .views import returnHomePage, restaurantDetailsPage, saveRestaurant, favoritesPage
from . import views

urlpatterns = [
    path('', returnHomePage, name='home'),  # Home page
    path('restaurants/', views.restaurants_view, name='restaurants'),  # Restaurant list page
    path('restaurants.html', views.restaurants_view, name='restaurants_html'),  # Also maps to the same view (optional)
    path('restaurant/<str:restaurant_id>/', restaurantDetailsPage, name='details'),  # Restaurant details page
    path('save/<str:restaurant_id>/', saveRestaurant, name='save'),  # Save a restaurant
    path('saved/', favoritesPage, name='saved'),  # Favorites page with trailing slash
]
