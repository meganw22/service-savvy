from django.shortcuts import render , get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views import generic
from .models import Ticket, JOB_CATEGORY, PRIORITY

# Create your views here.
class TicketListView(generic.ListView):
    queryset = Ticket.objects.all()
    template_name = "tickets/tickets.html"
    paginate_by = 5

class TicketDetailView(generic.DetailView):
    queryset = Ticket.objects.all()
    template_name = "tickets/ticket_detail.html"

class CreateTicketView(generic.CreateView):
    queryset = Ticket.objects.all()
    template_name = 'tickets/create_ticket.html'
    fields = ['title', 'job_category', 'job_description', 'location', 'priority' ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['JOB_CATEGORY'] = JOB_CATEGORY
        context['PRIORITY'] = PRIORITY
        return context

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return '/tickets/'