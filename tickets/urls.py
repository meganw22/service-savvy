from . import views
from django.urls import path
from .views import (
    TicketListView, TicketDetailView, CreateTicketView, 
    TicketUpdateView, TicketDeleteView, delete_comment, complete_ticket
    )

urlpatterns = [
    path("", TicketListView.as_view(), name="tickets"),
    path('create/', CreateTicketView.as_view(), name='create_ticket'),
    path('<slug:slug>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<slug:slug>/update/', TicketUpdateView.as_view(), name='update_ticket'),
    path('<slug:slug>/delete/', TicketDeleteView.as_view(), name='delete_ticket'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('tickets/<slug:ticket_slug>/complete/', views.complete_ticket, name='complete_ticket'),
]