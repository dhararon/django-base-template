import logging

from django.core.management.base import BaseCommand, CommandError

from apps.users.models import UserModel

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Add super user privileges to one user by email"

    def add_arguments(self, parser):
        parser.add_argument("email", type=str)

    def handle(self, *args, **options):  # noqa:ARG002
        email = options["email"]
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist as e:
            raise CommandError(f"The {email} does not exists.") from e
        else:
            user.is_staff = True
            user.is_superuser = True
            user.save()
            logger.info("User was converted to admin user", extra={"email": email})
