# camera_config_app/__init__.py
from django.urls import path, include

urlpatterns = [
    path('', include('camera_config_app.urls')),
    # Add other URL patterns here if needed
]
