from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Prefix for user-related routes
    path('', include('main.urls')),  # Main app routes start from the root
]

def catch_all_view(request, path):
    return HttpResponse(f"Path not found: {path}", status=404)

urlpatterns += [path('<path:path>', catch_all_view)]