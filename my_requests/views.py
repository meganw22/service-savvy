from django.shortcuts import render
from django.views import generic
from .models import create_ticket

class TicketList(generic.ListView):
    model = create_ticket