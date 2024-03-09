from . import views
from django.urls import path

urlpatterns = [
    path('requests/', views.TicketList.as_view(), name='my-requests'),
]