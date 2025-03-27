from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from model_utils import Choices
from model_utils.fields import UUIDField
from model_utils.models import SoftDeletableModel, StatusModel, UUIDModel

from .managers import UserManager


class UserModel(StatusModel, UUIDModel, SoftDeletableModel, AbstractBaseUser, PermissionsMixin):
    STATUS = Choices("pending", "active", "banned", "suspended")

    id = UUIDField(primary_key=True, version=4, editable=False)
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField("first name", max_length=30, blank=True)
    last_name = models.CharField("last name", max_length=30, blank=True)

    date_joined = models.DateTimeField("date joined", auto_now_add=True)
    last_login = models.DateTimeField("last login", null=True, blank=True)

    is_active = models.BooleanField("active", default=True)
    is_superuser = models.BooleanField("is_admin", default=True)
    is_staff = models.BooleanField("is_staff", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        db_table = "users_users"

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between."""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name
