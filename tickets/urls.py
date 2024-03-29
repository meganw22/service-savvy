from . import views
from django.urls import path
from .views import TicketListView, TicketDetailView, CreateTicketView, TicketUpdateView, TicketDeleteView, CommentDeleteView

urlpatterns = [
    path("", TicketListView.as_view(), name="tickets"),
    path('create/', CreateTicketView.as_view(), name='create_ticket'),
    path('<slug:slug>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<slug:slug>/update/', TicketUpdateView.as_view(), name='update_ticket'),
    path('<slug:slug>/delete/', TicketDeleteView.as_view(), name='delete_ticket'),
    path('<slug:slug>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]
