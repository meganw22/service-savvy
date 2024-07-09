from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import About
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# About Me View
@login_required
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


# Edit About View
class EditAboutView(LoginRequiredMixin, generic.UpdateView):
    """View to edit the users details"""
    model = About
    template_name = "about/edit_about.html"
    fields = ['full_name', 'job_title', 'email', 'tel']
    success_url = reverse_lazy('about')

    def form_valid(self, form):
        messages.success(self.request, 'Changes saved successfully!')
        return super().form_valid(form)
