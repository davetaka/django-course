from django.test import TestCase
from django.core import mail
from django.test.client import Client
from django.urls import reverse
from django.conf import settings

from .models import Course

class ContactCourseTestCase(TestCase):

    def setUp(self):
        self.course = Course.objects.create(name="Django", slug="django")

    def tearDown(self):
        self.course.delete()

    # @classmethod
    # def setUpClass(cls):
    #     return super().setUpClass()

    # @classmethod
    # def tearDownClass(cls):
    #     return super().tearDownClass()

    def test_contact_form_error(self):
        data = { "name": "Fulano de Tal", "email": "", "message": "" }
        client = Client()
        path = reverse("courses:details", args=[self.course.slug])
        response = client.post(path)

        self.assertFormError(response, "form", "email", "Este campo é obrigatório.")
        self.assertFormError(response, "form", "message", "Este campo é obrigatório.")


    def test_contact_form_success(self):
        data = { "name": "Fulano de Tal", "email": "admin@admin.com", "message": "OK" }
        client = Client()
        path = reverse("courses:details", args=[self.course.slug])
        response = client.post(path)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])