from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.template.loader import render_to_string
from .models import Ticket, JOB_CATEGORY, PRIORITY, Comment
from django.urls import reverse_lazy
from .forms import TicketUpdateForm

# Ticket List View
class TicketListView(ListView):
    queryset = Ticket.objects.all()
    template_name = "tickets/tickets.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by', 'priority')
        
        if sort_by == 'priority':
            queryset = queryset.order_by('priority')
        elif sort_by == 'created_on':
            queryset = queryset.order_by('created_on')
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_sort_by'] = self.request.GET.get('sort_by', 'priority')  # Default to 'priority' if not provided
        return context

# Ticket Detail View
class TicketDetailView(DetailView):
    model = Ticket
    template_name = "tickets/ticket_detail.html"
    slug_field = 'slug'

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        queryset = self.get_queryset()
        return get_object_or_404(queryset, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = self.object
        context['comments'] = ticket.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        ticket = self.get_object()
        body = request.POST.get('body')
        if body:
            comment = Comment.objects.create(ticket=ticket, username=request.user, body=body)
            comment.save()
        return redirect('ticket_detail', slug=ticket.slug)

# Create ticket View
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

# Update Ticket View
class TicketUpdateView(UpdateView):
    model = Ticket
    template_name = 'tickets/update_ticket.html'
    fields = ['title', 'job_category', 'job_description', 'location', 'priority' ]
    success_url = reverse_lazy('tickets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['JOB_CATEGORY'] = JOB_CATEGORY
        context['PRIORITY'] = PRIORITY
        return context

    def update_ticket(request, slug):
        ticket = get_object_or_404(Ticket, slug=slug)
    
        if request.method == 'POST':
            form = TicketUpdateForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('ticket_detail', slug=slug)
        else:
            form = TicketUpdateForm(instance=ticket)
    
        context = {
            'form': form,
            'ticket': ticket,
            'JOB_CATEGORY': JOB_CATEGORY,
            'PRIORITY': PRIORITY,
        }
        return render(request, 'tickets/update_tickets.html', context)