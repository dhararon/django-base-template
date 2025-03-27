from __future__ import annotations

from configurations import values

from settings.admin.base import AdminBaseConfig


class DevConfig(AdminBaseConfig):
    SECRET_KEY = values.Value()

    @classmethod
    def setup(cls: object) -> None:
        super().setup()
        cls._configure_logs()

    # STATIC FILES CONFIGURATION
    @property
    def STATIC_ROOT(self) -> str:  # noqa: N802
        return str(self.BASE_DIR + "/staticfiles")

    @property
    def STATIC_URL(self) -> str:  # noqa: N802
        return "static/"

    def get_django_apps_b(self) -> list[str]:
        return [
            "django_extensions",
        ]

    def get_third_party_apps(self) -> list[str]:
        apps = super().get_third_party_apps()
        return [
            *apps,
            "whitenoise.runserver_nostatic",
            "django.contrib.staticfiles",
            "debug_toolbar",
        ]
