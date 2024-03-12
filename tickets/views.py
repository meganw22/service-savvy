from django.shortcuts import render , get_object_or_404
from django.views import generic
from .models import create_ticket

# Create your views here.
class TicketList(generic.ListView):
    queryset = create_ticket.objects.all()
    template_name = "tickets/index.html"
    # paginate_by = 6

def post_detail(request, slug):
    queryset = create_ticket.objects.filter(priority=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "tickets/post_detail.html",
        {
            "post": post,
            "coder": "Megan Walford",
        },
    )