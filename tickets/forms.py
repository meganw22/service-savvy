from django import forms
from .models import Ticket, Comment

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'job_category', 'job_description', 'location', 'priority']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)