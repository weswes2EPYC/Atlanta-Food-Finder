from django.urls import path
from . import views
from .views import returnHomePage

urlpatterns = [
    path('', returnHomePage, name='home'),
    path('restaurants/', views.restaurants_view, name='restaurants'),
    path('restaurants.html', views.restaurants_view, name='restaurants')
    # ... other url patterns
]