from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # You can add extra fields here if needed
    # e.g., bio, profile picture, preferences, etc.
