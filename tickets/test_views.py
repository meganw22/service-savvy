from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Ticket, Comment

class TicketDetailViewTest(TestCase):
    def setUp(self):
        # Create a ticket
        self.ticket = Ticket.objects.create(title='Test Ticket',
                                            job_description='Test job description',
                                            location='Test location',
                                            username=self.user)

        # Create comments associated with the ticket
        self.comment1 = Comment.objects.create(ticket=self.ticket,
                                            username=self.user,
                                            body='Test comment 1')
        self.comment2 = Comment.objects.create(ticket=self.ticket,
                                            username=self.user,
                                            body='Test comment 2')

    def test_comments_displayed(self):
        # Ensure comments are displayed correctly
        response = self.client.get(reverse('ticket_detail', args=[self.ticket.slug]))
        self.assertContains(response, 'Test comment 1')
        self.assertContains(response, 'Test comment 2')

    def test_no_comments_message(self):
        # Ensure message is displayed when there are no comments
        self.ticket.comments.all().delete()  # Delete existing comments
        response = self.client.get(reverse('ticket_detail', args=[self.ticket.slug]))
        self.assertContains(response, 'No comments just yet...')

    def test_add_comment_form_displayed(self):
        # Ensure add comment form is displayed when user is authenticated
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('ticket_detail', args=[self.ticket.slug]))
        self.assertContains(response, 'Leave a comment as testuser')

    def test_comment_submission(self):
        # Ensure comment submission works
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('ticket_detail', args=[self.ticket.slug]), data={'body': 'Test comment'})
        self.assertEqual(response.status_code, 302)

    def test_delete_comment(self):
        # Ensure comment deletion works
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('delete_comment', args=[self.comment1.id]))
        self.assertEqual(response.status_code, 302) 
        self.assertFalse(Comment.objects.filter(id=self.comment1.id).exists())