from . import views
from django.urls import path

# 'upn' stands for Url Pattern (my name convention).
urlpatterns = [
    path("", views.home, name="home-upn"),
    path("process-mistake", views.processMistake, name="process-mistake-upn"),
    path("doomsday/", views.doomsdayDeviceActivated, name="doomsday-upn"),
]
