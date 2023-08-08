from ..base import BaseConfig
from .admin_interface import AdminInterfaceConfig


class DevConfig(AdminInterfaceConfig, BaseConfig):
    # Secret Key
    SECRET_KEY = "django-insecure-c66%v+l*w)lh2f!ionbc(#z=e=38gnqsdm#=7^5vgoi1)s8i@h"
    ROOT_URLCONF = "urls.admin"

    @classmethod
    def setup(cls):
        super(DevConfig, cls).setup()
        cls._configure_logs()

    # STATIC FILES CONFIGURATION
    @property
    def STATIC_ROOT(self):
        return self.BASE_DIR + "/staticfiles"

    @property
    def STATIC_URL(self):
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
