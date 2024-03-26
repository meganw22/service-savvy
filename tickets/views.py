from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView
from django.template.loader import render_to_string
from .models import Ticket, JOB_CATEGORY, PRIORITY

# Create your views here.
class TicketListView(ListView):
    queryset = Ticket.objects.all()
    template_name = "tickets/tickets.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by', 'priority')
        
        if sort_by == 'priority':
            queryset = queryset.order_by('priority')
        elif sort_by == 'username':
            queryset = queryset.order_by('username')
        elif sort_by == 'created_on':
            queryset = queryset.order_by('created_on')
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_sort_by'] = self.request.GET.get('sort_by', 'priority')  # Default to 'priority' if not provided
        return context

class TicketDetailView(DetailView):
    model = Ticket
    template_name = "tickets/ticket_detail.html"

class CreateTicketView(CreateView):
    model = Ticket
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