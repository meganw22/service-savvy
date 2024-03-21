from . import views
from django.urls import path
from .views import TicketListView, TicketDetailView

urlpatterns = [
    path("<slug:slug>/", TicketDetailView.as_view(), name="ticket_detail"),
    path("", TicketListView.as_view(), name="tickets"),
]
