from django.db import models
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
class create_ticket(models.Model):
    title = models.CharField(max_length=200)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="my_requests"
    )
    job_category = models.CharField(choices=JOB_CATEGORY, default=0)
    job_description = models.CharField(max_length=400, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    priority = models.IntegerField(choices=PRIORITY, default=0)

    class Meta:
        ordering = ["priority"]

    def __str__(self):
        return f"Request: {self.title}"