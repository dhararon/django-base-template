from __future__ import annotations

from configurations import values

from settings.api.base import APIBaseConfig


class DevConfig(APIBaseConfig):
    SECRET_KEY = values.Value()

    @classmethod
    def setup(cls: object) -> None:
        super().setup()
        cls._configure_logs()

    def get_django_apps_b(self) -> list[str]:
        return [
            "django_extensions",
        ]

    def get_third_party_apps(self) -> list[str]:
        apps = super().get_third_party_apps()
        return [
            *apps,
            "debug_toolbar",
        ]
