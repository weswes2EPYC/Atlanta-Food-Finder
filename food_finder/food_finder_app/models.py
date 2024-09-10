from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    API_id = models.CharField(max_length=255, unique = True)

    def __str__(self):
        return self.API_id

class Favorites(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    favorite_restaurants = models.ManyToManyField(Restaurant, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'restaurant')

    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name}"