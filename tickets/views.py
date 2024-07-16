from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Ticket, JOB_CATEGORY, PRIORITY, Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now


class TicketListView(LoginRequiredMixin, ListView):
    """
    Display a paginated list of all created tickets, Users are able to sort 
    by various filters and display only their own tickets
    """
    queryset = Ticket.objects.all()
    template_name = "tickets/tickets.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        show_own_tickets = self.request.GET.get('own_tickets', False)
        if show_own_tickets:
            queryset = queryset.filter(username=self.request.user)

        sort_by = self.request.GET.get('sort_by', 'priority_high')
        if sort_by == 'priority_high':
            queryset = queryset.filter(is_complete=False).order_by(
                'priority', 'created_on')
        elif sort_by == 'priority_low':
            queryset = queryset.filter(is_complete=False).order_by(
                '-priority', 'created_on')
        elif sort_by == 'created_newest':
            queryset = queryset.filter(is_complete=False).order_by(
                '-created_on', 'priority')
        elif sort_by == 'created_oldest':
            queryset = queryset.filter(is_complete=False).order_by(
                'created_on', 'priority')
        elif sort_by == 'completed':
            queryset = queryset.filter(is_complete=True).order_by(
                '-completed_at', 'created_on')
        else:
            queryset = queryset.order_by('priority', 'created_on')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_sort_by'] = self.request.GET.get(
            'sort_by', 'priority_high')
        context['show_own_tickets'] = self.request.GET.get(
            'own_tickets', False)
        return context


class TicketDetailView(DetailView):
    """
    Individual ticket detailed view with option to add comments to ticket.
    """
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
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        ticket = self.get_object()
        body = request.POST.get('body')
        if body:
            comment = Comment.objects.create(
                ticket=ticket, username=request.user, body=body)
            comment.save()
            messages.success(self.request, 'Comment created successfully')
        return redirect('ticket_detail', slug=ticket.slug)


class CreateTicketView(CreateView):
    """View to create a new ticket"""
    model = Ticket
    template_name = 'tickets/create_ticket.html'
    fields = [
        'title', 'job_category', 'job_description', 'location', 'priority'
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['JOB_CATEGORY'] = JOB_CATEGORY
        context['PRIORITY'] = PRIORITY
        return context

    def form_valid(self, form):
        title = form.cleaned_data['title']
        if Ticket.objects.filter(title=title).exists():
            form.add_error('title', 'A ticket with this title already exists.')
            return self.form_invalid(form)
        form.instance.username = self.request.user
        messages.success(self.request, 'Ticket created successfully')
        return super().form_valid(form)

    def get_success_url(self):
        return '/tickets/'


class TicketUpdateView(UpdateView):
    """Update Ticket content view"""
    model = Ticket
    template_name = 'tickets/update_ticket.html'
    fields = [
        'title', 'job_category', 'job_description', 'location', 'priority'
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['JOB_CATEGORY'] = JOB_CATEGORY
        context['PRIORITY'] = PRIORITY
        return context

    def form_valid(self, form):
        form.instance.username = self.request.user
        if form.instance.is_complete:
            form.instance.completed_by = self.request.user
            form.instance.completed_at = now()

        messages.success(self.request, 'Ticket updated successfully')
        return super().form_valid(form)


class TicketDeleteView(DeleteView):
    """Delete Ticket View"""
    model = Ticket
    success_url = reverse_lazy('tickets')
    template_name = 'tickets/delete_ticket.html'


def delete_comment(request, comment_id):
    """Delete User Comment View"""
    comment = get_object_or_404(Comment, id=comment_id)
    ticket_slug = comment.ticket.slug
    if comment.username == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
    else:
        messages.error(
            request, 'You do not have permission to delete this comment.')
    return redirect('ticket_detail', slug=ticket_slug)


@login_required
def complete_ticket(request, ticket_slug):
    """
    If staff authenticated, View to allow completion of tickets, marking
    ticket as complete and setting a completed timestamp.
    """
    ticket = get_object_or_404(Ticket, slug=ticket_slug)

    if not request.user.is_superuser and not request.user.is_staff:
        messages.error(request, "You do not have permission to complete this ticket.")
        return redirect('ticket_detail', slug=ticket.slug)

    if ticket.is_complete:
        ticket.is_complete = False
        ticket.completed_by = None
        ticket.completed_at = None
        messages.success(request, "Ticket marked as 'Incomplete'")
    else:
        ticket.is_complete = True
        ticket.completed_by = request.user
        ticket.completed_at = now()
        messages.success(request, "Ticket marked as 'Complete'")
    ticket.save()

    return redirect('ticket_detail', slug=ticket.slug)
