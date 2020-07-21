from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactCourse(forms.Form):

    name = forms.CharField(label="Nome", max_length=100)
    email = forms.CharField(label="E-mail")
    message = forms.CharField(label="Mensagem/Dúvida", widget=forms.Textarea)

    def send_mail(self, course):
        subject = f"{course.name} Curso"

        context = {
            "name": self.cleaned_data["name"],
            "email": self.cleaned_data["email"],
            "message": self.cleaned_data["message"]
        }

        message = f"Nome:{context["name"]};E-mail:{context["email"]};{context["message"]}"

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                  [settings.CONTACT_EMAIL])
