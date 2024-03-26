from . import views
from django.urls import path
from .views import TicketListView, TicketDetailView, CreateTicketView

urlpatterns = [
    path("", TicketListView.as_view(), name="tickets"),
    path('create/', CreateTicketView.as_view(), name='create_ticket'),
    path('<slug:slug>/', TicketDetailView.as_view(), name='ticket_detail'),

]
