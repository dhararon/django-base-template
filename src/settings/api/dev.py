# Standard Library
import os

from ..base import BaseConfig
from .rest_framework import BaseRestFrameworkConfig, BaseSpectacularConfig


class DevConfig(BaseRestFrameworkConfig, BaseSpectacularConfig, BaseConfig):
    # Secret Key
    SECRET_KEY = (
        "django-insecure-api-c66%v+l*w)lh2f!ionbc(#z=e=38gnqsdm#=7^5vgoi1)s8i@h"
    )
    ROOT_URLCONF = "urls.api"
    EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_USE_TLS = False

    def get_third_party_apps(self):
        return ["rest_framework", "knox", "drf_spectacular"]
