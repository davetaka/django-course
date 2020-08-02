from simplemoc.courses.models import Enrollments
from django.template import Library

register = Library()


@register.inclusion_tag("courses/templatetags/my_courses.html")
def my_courses(user):
    enrollments = Enrollments.objects.filter(user=user)

    context = {
        "enrollments": enrollments
    }

    return context


@register.simple_tag
def load_my_courses(user):
    return Enrollments.objects.filter(user=user)
