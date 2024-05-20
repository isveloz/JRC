# core/tests.py

from django.test import TestCase # type: ignore
from django.urls import reverse # type: ignore

class CoreViewsTestCase(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')
