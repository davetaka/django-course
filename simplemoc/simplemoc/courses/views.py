from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollments
from .forms import ContactCourse


def index(request):
    courses = Course.objects.all()
    template_name = "courses/index.html"
    context = {
        "courses": courses
    }
    return render(request, template_name, context)


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {}

    if request.method == "POST":
        form = ContactCourse(request.POST)

        if form.is_valid():
            form.send_mail(course)
            form = ContactCourse()
            context["is_valid"] = True

    else:
        form = ContactCourse()

    context["course"] = course
    context["form"] = form

    template_name = "courses/details.html"
    return render(request, template_name, context)


@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)

    enrollment, created = Enrollments.objects.get_or_create(
        user=request.user,
        course=course
    )

    if created:
        messages.success(request, "Você foi inscrito no curso")
    else:
        messages.info(request, "Você já está inscrito no curso")

    return redirect("accounts:dashboard")


@login_required
def announcements(request, slug):
    course = get_object_or_404(Course, slug=slug)

    if not request.user.is_staff:
        enrollment = get_object_or_404(
            Enrollments,
            user=request.user,
            course=course
        )

        if not enrollment.is_approved():
            messages.error(request, "A sua inscrição está pendente")
            return redirect("accounts:dashboard")

    template = "courses/announcements.html"
    context = {
        "course": course,
        "announcements": course.announcements.all()
    }
    return render(request, template, context)


@login_required
def undo_enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(
        Enrollments, user=request.user, course=course
    )
    if request.method == "POST":
        enrollment.delete()
        messages.success(request, "Sua inscrição foi cancelada com sucesso")
        return redirect("accounts:dashboard")

    template = "courses/undo_enrollment.html"
    context = {
        "enrollment": enrollment,
        "course": course
    }

    return render(request, template, context)