from . import views
from django.urls import path
from .views import EditAboutView

urlpatterns = [
    path('', views.about_me, name='about'),
    path('edit/<int:pk>/', EditAboutView.as_view(), name='edit-about'),
]
