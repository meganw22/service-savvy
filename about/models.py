from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    member_since = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name