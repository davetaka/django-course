from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("entrar/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("cadastre-se/", views.register, name="register"),
    path("sair/", LogoutView.as_view(next_page="core:home"), name="logout")
]
