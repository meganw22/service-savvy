from django.shortcuts import render , get_object_or_404
from django.views import generic
from .models import create_ticket

# Create your views here.
class TicketList(generic.ListView):
    queryset = create_ticket.objects.all()
    template_name = "my_requests/index.html"
    # paginate_by = 6