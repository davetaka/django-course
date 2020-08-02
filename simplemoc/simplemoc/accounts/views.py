from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from simplemoc.core.utils import generate_hash_key

from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset


User = get_user_model()


@login_required
def dashboard(request):
    template_name = "accounts/dashboard.html"
    context = {}
    return render(request, template_name, context)


def register(request):
    template_name = "accounts/register.html"
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data["password1"]
            )
            login(request, user)
            return redirect("core:home")
    else:
        form = RegisterForm()

    context = {"form": form}

    return render(request, template_name, context)


def password_reset(request):
    template_name = "accounts/password_reset.html"
    form = PasswordResetForm(request.POST or None)
    context = {}

    if form.is_valid():
        form.save()
        messages.success(
            request, "Um e-mail foi enviado para você com novos detalhes de como criar uma nova senha")

    context["form"] = form

    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = "accounts/password_reset_confirm.html"
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)

    if form.is_valid():
        form.save()
        context["success"] = True

    context["form"] = form
    return render(request, template_name, context)


@login_required
def edit(request):
    template_name = "accounts/edit.html"
    context = {}

    if request.method == "POST":
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            messages.success(
                request, "Os dados foram alterados com sucesso!!!")
            return redirect("accounts:dashboard")

    else:
        form = EditAccountForm(instance=request.user)

    context["form"] = form
    return render(request, template_name, context)


@login_required
def change_password(request):
    template_name = "accounts/change_password.html"
    context = {}

    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Sua senha foi alterada com sucesso, faça o login novamente")
            return redirect("accounts:dashboard")

    else:
        form = PasswordChangeForm(user=request.user)
    context["form"] = form

    return render(request, template_name, context)
