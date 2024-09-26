from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SavedRestaurants(models.Model):
    restaurant_id = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username", db_column="username")

    class Meta:
        unique_together = (('username', 'restaurant_id'))

def get_saved_restaurants(username):
    return SavedRestaurants.objects.filter(username=username)

def is_restaurant_saved(username, restaurant_id):
    return SavedRestaurants.objects.filter(username__username=username, restaurant_id=restaurant_id).exists()

def save_restaurant(username, restaurant_id):
    restaurant = SavedRestaurants(username=username, restaurant_id=restaurant_id)
    restaurant.save()

def unsave_restaurant(username, restaurant_id):
    SavedRestaurants.objects.filter(username=username, restaurant_id=restaurant_id).delete()