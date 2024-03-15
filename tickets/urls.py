from . import views
from django.urls import path

urlpatterns = [
    path('', views.TicketList.as_view(), name='tickets'),
]
