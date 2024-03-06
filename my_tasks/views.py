from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_tasks(request):
    return HttpResponse("Savvy Tasks")