from settings.base import BaseConfig

from .admin_interface import AdminInterfaceConfig


class DevConfig(AdminInterfaceConfig, BaseConfig):
    # Secret Key
    SECRET_KEY = ""
    ROOT_URLCONF = "urls.admin"

    @classmethod
    def setup(cls):
        super().setup()
        cls._configure_logs()

    # STATIC FILES CONFIGURATION
    @property
    def STATIC_ROOT(self):  # noqa: N802
        return self.BASE_DIR + "/staticfiles"

    @property
    def STATIC_URL(self):  # noqa: N802
        return "static/"

    def get_django_apps_b(self):
        return [
            "django_extensions",
        ]

    def get_third_party_apps(self):
        return [
            "whitenoise.runserver_nostatic",
            "debug_toolbar",
        ]
