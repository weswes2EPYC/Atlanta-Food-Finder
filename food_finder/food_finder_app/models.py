from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    API_id = models.CharField(max_length=255)
