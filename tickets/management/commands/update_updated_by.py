# tickets/management/commands/update_updated_by.py
from django.core.management.base import BaseCommand
from tickets.models import Ticket

class Command(BaseCommand):
    help = 'Update the updated_by field for tickets to the username of the person who created the ticket.'

    def handle(self, *args, **kwargs):
        tickets = Ticket.objects.filter(updated_by__isnull=True)
        for ticket in tickets:
            ticket.updated_by = ticket.username
            ticket.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully updated ticket {ticket.title} (ID: {ticket.id})'
                )
            )
        self.stdout.write(self.style.SUCCESS('All relevant tickets updated.'))
