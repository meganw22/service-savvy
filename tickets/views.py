from django.shortcuts import render , get_object_or_404
from django.views import generic
from .models import Ticket

# Create your views here.
class TicketList(generic.ListView):
    queryset = Ticket.objects.all()
    template_name = "tickets/index.html"
    # paginate_by = 6

# def post_detail(request, slug):
#     queryset = Ticket.objects.filter(priority=1)
#     post = get_object_or_404(queryset, slug=slug)

#     return render(
#         request,
#         "tickets/post_detail.html",
#         {
#             "post": post,
#             "coder": "Megan Walford",
#         },
#     )