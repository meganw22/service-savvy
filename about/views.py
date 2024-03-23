from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )