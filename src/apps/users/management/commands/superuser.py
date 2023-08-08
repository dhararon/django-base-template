# Third Party Stuff
# Third Party Stuff
from django.core.management.base import BaseCommand, CommandError

# Django Base Template
from apps.users.models import UserModel


class Command(BaseCommand):
    help = "Add super user privileges to one user by email"

    def add_arguments(self, parser):
        parser.add_argument("email", type=str)

    def handle(self, *args, **options):
        email = options["email"]
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            raise CommandError(f"The {email} does not exists.")
        else:
            user.is_staff = True
            user.is_superuser = True
            user.save()
            print(f"{email} was converted to admin user")
