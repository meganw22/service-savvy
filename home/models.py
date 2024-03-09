from django.db import models
# from django.contrib.auth.models import User, AbstractUser

# # Create your models here.

# class CustomUser(AbstractUser):
#     REQUESTOR = 'requestor'
#     FIXER = 'fixer'
#     USER_TYPES = [
#         (REQUESTOR, 'Requestor'),
#         (FIXER, 'Fixer'),
#     ]
#     user_type = models.CharField(choices=USER_TYPES, max_length=20)

# class create_account(models.Model):
    
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)