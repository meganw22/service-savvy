from django.db import models

# Create your models here.
class About(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    member_since = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name