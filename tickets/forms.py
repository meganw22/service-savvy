from django import forms
from .models import Ticket

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'job_category', 'job_description', 'location', 'priority']