from . import views
from django.urls import path

urlpatterns = [
    path('tickets/', views.TicketList.as_view(), name='tickets'),
]