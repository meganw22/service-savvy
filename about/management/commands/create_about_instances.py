from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from about.models import About

class Command(BaseCommand):
    help = 'Create About instances for all existing users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            if not hasattr(user, 'about'):
                About.objects.create(
                    user=user,
                    full_name=user.get_full_name() or user.username,
                    job_title='',
                    tel='',
                    member_since=user.date_joined
                )
                self.stdout.write(self.style.SUCCESS(f'About instance created for user: {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'About instance already exists for user: {user.username}'))
