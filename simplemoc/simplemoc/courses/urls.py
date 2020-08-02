from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:slug>", views.details, name="details"),
    path("<str:slug>/inscricao", views.enrollment, name="enrollment"),
    path("<str:slug>/anuncios", views.announcements, name="announcements"),
    # path("/<int:pk>", views.details, name="details")
]
