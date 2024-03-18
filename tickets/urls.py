from . import views
from django.urls import path

urlpatterns = [
    path('', views.TicketList.as_view(), name='tickets'),
    # path('tickets/<slug:slug>/', views.TicketDetailView.as_view(), name='ticket_detail'),
]
