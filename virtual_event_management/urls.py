from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page for managing the project
    path('', include('events.urls')),  # Include URLs from your app
]
