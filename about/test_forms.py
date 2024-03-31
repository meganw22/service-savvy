from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import About

class EditAboutViewTest(TestCase):
    def test_edit_about_view(self):
        # Create a user for testing
        user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(user)

        # Access the edit about view
        response = self.client.get(reverse('about'))

        # Check if the view returns a successful response
        self.assertEqual(response.status_code, 200)

    def test_form_valid(self):
        # Create a user for testing
        user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(user)

        # Create an About object for the user
        about = About.objects.create(user=user)

        # Data to submit in the form
        data = {
            'full_name': 'John Doe',
            'job_title': 'Software Developer',
            'email': 'john@example.com',
            'tel': '1234567890'
        }

        # Access the edit about view and submit the form
        response = self.client.post(reverse('about'), data)

        # Check if the form submission was successful
        self.assertRedirects(response, reverse('about'))
        about.refresh_from_db()
        self.assertEqual(about.full_name, 'John Doe')
        self.assertEqual(about.job_title, 'Software Developer')
        self.assertEqual(about.email, 'john@example.com')
        self.assertEqual(about.tel, '1234567890')