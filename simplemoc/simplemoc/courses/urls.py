from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:slug>", views.details, name="details")
    # path("/<int:pk>", views.details, name="details")
]
