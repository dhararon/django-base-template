from __future__ import annotations

from settings.admin.admin_interface import AdminInterfaceConfig
from settings.common.base import BaseConfig


class AdminBaseConfig(AdminInterfaceConfig, BaseConfig):
    ROOT_URLCONF = "urls.admin"

    def get_django_apps_t(self) -> list:
        return [
            "admin_interface",
            "colorfield",
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
        ]
