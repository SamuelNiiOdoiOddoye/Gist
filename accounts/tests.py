from django.template import response
from django.test import TestCase
from django.contrib.auth import get_user, get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'testPass123',
            'password2': 'testPass123',
        })

        self.assertEqual(response.status_code, 302)  # Check for redirect after successful signup
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'testuser@gmail.com')