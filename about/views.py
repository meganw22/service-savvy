from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
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

class EditAboutView(generic.UpdateView):
    model = About
    template_name = "about/edit_about.html"
    fields = ['full_name', 'job_title', 'email', 'tel']
    success_url = reverse_lazy('about')

    def form_valid(self, form):
        messages.success(self.request, 'Changes saved successfully!')
        return super().form_valid(form)