from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course
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

    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )

    return redirect("accounts:dashboard")
