from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Creating different roles"

    def handle(self, *args, **options):
        admin_role, _ = Group.objects.get_or_create(name="Admin")
        regular_role , _ = Group.objects.get_or_create(name="Regular")

        self.stdout.write(self.style.SUCCESS('Roles Created Successfully'))