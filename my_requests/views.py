from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_requests(request):
    return HttpResponse("Savvy Requests")