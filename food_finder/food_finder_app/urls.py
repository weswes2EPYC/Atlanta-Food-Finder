from django.urls import path
from .import views

app_name = "food_finder_app"

urlpatterns = [
    path('route', views.route, name="route"),
    path('map', views.map, name="map"),
]