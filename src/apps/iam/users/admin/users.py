from __future__ import annotations

import typing

from django.contrib import admin

from apps.iam.users.models import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display: typing.ClassVar[list[str]] = ["id", "email"]
