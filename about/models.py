from django.db import models
from django.contrib.auth.models import User

# About Model
class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    member_since = models.DateTimeField()

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.pk and not self.member_since:
            self.member_since = self.user.date_joined
        super().save(*args, **kwargs)
