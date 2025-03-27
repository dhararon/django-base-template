from __future__ import annotations

from settings.api.rest_framework import BaseRestFrameworkConfig, BaseSpectacularConfig
from settings.common.base import BaseConfig


class APIBaseConfig(BaseRestFrameworkConfig, BaseSpectacularConfig, BaseConfig):
    ROOT_URLCONF: str = "urls.api"
    APPEND_SLASH: bool = True

    def get_django_apps_t(self) -> list:
        return [
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
        ]

    def get_third_party_apps(self) -> list[str]:
        apps = super().get_third_party_apps()
        return [
            *apps,
            "rest_framework",
            "knox",
            "drf_spectacular",
        ]
