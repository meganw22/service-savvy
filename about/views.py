from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the About page
    """
    about, created = About.objects.get_or_create(user=request.user)
    if created:
        # Set the user field to the currently logged-in user
        about.user = request.user
        about.save()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )