from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Prefix for user-related routes
    path('', include('main.urls')),  # Main app routes start from the root
]