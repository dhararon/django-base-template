# Standard Library
import os
import sys
from pathlib import Path

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
    DEBUG: bool = bool(os.getenv("DEBUG", "1"))

    AUTH_USER_MODEL: str = "users.UserModel"
    WSGI_APPLICATION: str = "wsgi.application"
    APPEND_SLASH: bool = True

    @property
    def BASE_DIR(self):  # noqa: N802
        # Get /app/settings/common/base.py and get 2 parent for /app response
        base_dir = Path(__file__).parents[2]

        # Add apps and account_statement as PYTHONPATH
        base_app_dir = base_dir / "apps"

        sys.path.append(str(base_app_dir))
        return base_dir
