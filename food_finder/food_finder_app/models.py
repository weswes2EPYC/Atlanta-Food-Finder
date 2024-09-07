from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    API_id = models.CharField(max_length=255)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_restaurants = models.ManyToManyField(Restaurant, related_name='favorited_by')