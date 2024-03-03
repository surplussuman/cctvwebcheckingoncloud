'''# camera_config_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('configure-camera-feed/', views.configure_camera_feed, name='configure_camera_feed'),
    #path('configure-camera-feed/success/', views.configure_camera_feed_success, name='configure_camera_feed_success'),
]'''

from django.urls import path
from . import views

urlpatterns = [
    path('video_feed/', views.video_feed, name='video_feed'),
    path('configure-camera-feed/', views.configure_camera_feed, name='configure_camera_feed'),
]
