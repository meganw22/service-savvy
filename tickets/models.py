from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

JOB_CATEGORY = (
    (0, "Choose Type"),
    (1, "Plumbing"),
    (2, "Lighting"),
    (3, "Heating"),
    (4, "Cleaning"),
    (5, "Vending Services"),
    (6, "Air Conditioning"),
    (7, "Waste"),
    (8, "Other"),
)

PRIORITY = (
    (0, "Priority Level"),
    (1, "High (<2 hours)"),
    (2, "Medium (<1 day)"),
    (3, "Low (1 day +)"),
)

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_tickets"
    )
    job_category = models.IntegerField(choices=JOB_CATEGORY, default=0)
    job_description = models.TextField(max_length=400, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.TextField(max_length=200)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    is_complete = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["priority"]

    def __str__(self):
        return f"Request: {self.title}"

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Ticket, self).save(*args, **kwargs)


class Comment(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="comments"
    )
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.username}"

class Archive(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    archived_at = models.DateTimeField(auto_now_add=True)