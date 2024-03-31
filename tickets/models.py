from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

JOB_CATEGORY = (
    (0, "Plumbing"),
    (1, "Lighting"),
    (2, "Heating"),
    (3, "Cleaning"),
    (4, "Vending Services"),
    (5, "Air Conditioning"),
    (6, "Waste"),
    (7, "Other"),
)

PRIORITY = (
    (0, "High (<2 hours)"),
    (1, "Medium (<1 day)"),
    (2, "Low (1 day +)"),
)

# Ticket Model
class Ticket(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(null=True, unique=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_tickets")
    job_category = models.IntegerField(choices=JOB_CATEGORY, default=0)
    job_description = models.TextField(max_length=400, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.TextField(max_length=200)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    is_complete = models.BooleanField(default=False)
    completed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name="completed_tickets")
    completed_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Request: {self.title}"

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Ticket, self).save(*args, **kwargs)

# Comment Model
class Comment(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="comments")
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.body} by {self.username}"

# Archive Model - not utilised
class Archive(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
