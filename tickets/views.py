from django.shortcuts import render , get_object_or_404
from django.views import generic
from .models import Ticket

# Create your views here.
class TicketListView(generic.ListView):
    queryset = Ticket.objects.all()
    template_name = "tickets/tickets.html"
    # model = Ticket
    # template_name = "tickets/index.html"
    # paginate_by = 6

class TicketDetailView(generic.DetailView):
    queryset = Ticket.objects.all()
    template_name = "tickets/ticket_detail.html"
