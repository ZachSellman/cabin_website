from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="cabin-homepage"),
    path("about/", views.about, name="cabin-about"),
]
