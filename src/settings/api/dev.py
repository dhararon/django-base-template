# Standard Library
import os

from settings.base import BaseConfig

from .rest_framework import BaseRestFrameworkConfig, BaseSpectacularConfig


class DevConfig(BaseRestFrameworkConfig, BaseSpectacularConfig, BaseConfig):
    # Secret Key
    SECRET_KEY: str = ""
    ROOT_URLCONF: str = "urls.api"
    EMAIL_BACKEND: str = os.getenv("EMAIL_BACKEND")
    EMAIL_HOST: str = os.getenv("EMAIL_HOST")
    EMAIL_PORT: str = os.getenv("EMAIL_PORT")
    EMAIL_USE_TLS: bool = False

    def get_third_party_apps(self):
        return ["rest_framework", "knox", "drf_spectacular"]
