from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("entrar/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("cadastre-se/", views.register, name="register"),
    path("editar/", views.edit, name="edit"),
    path("alterar-senha/", views.edit_password, name="edit_password"),
    path("sair/", LogoutView.as_view(next_page="core:home"), name="logout")
]
