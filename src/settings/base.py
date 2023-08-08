# Standard Library
import os

# Third Party Stuff
from configurations import Configuration

from .apps import BaseAppConfig
from .database import BaseDatabaseConfig
from .django import (
    BaseInternationalizationConfig,
    BaseMiddlewareConfig,
    BaseStaticFilesConfig,
    BaseTemplateConfig,
    BaseURLConfig,
)
from .mail import BaseMailConfig
from .structlog import BaseStructlog


class BaseConfig(
    BaseDatabaseConfig,
    BaseAppConfig,
    BaseMiddlewareConfig,
    BaseTemplateConfig,
    BaseURLConfig,
    BaseInternationalizationConfig,
    BaseStaticFilesConfig,
    BaseStructlog,
    BaseMailConfig,
    Configuration,
):
    # Debugging
    DEBUG = bool(os.getenv("DEBUG", True))

    AUTH_USER_MODEL = "users.UserModel"
    WSGI_APPLICATION = "wsgi.application"
    APPEND_SLASH = True

    @property
    def BASE_DIR(self):
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
