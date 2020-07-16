from django.urls import path, include
from . import views

urlpatterns = [
    path("contato/", views.contact, name="contact"),
    path("", views.home, name="home")
]
