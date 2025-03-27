from django.core.management.base import BaseCommand, CommandError
from users.models import UserModel


class Command(BaseCommand):
    help: str = "Add super user privileges to one user by email"

    def add_arguments(self, parser: object) -> None:
        parser.add_argument("email", type=str)

    def handle(self, **options: dict) -> None:
        email = options["email"]
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist as e:
            msg = f"The {email} does not exists."
            raise CommandError(msg) from e
        else:
            user.is_staff = True
            user.is_superuser = True
            user.save()
