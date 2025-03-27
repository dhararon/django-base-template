# Standard Library
import sys
from pathlib import Path

# Third Party Stuff
from configurations import Configuration, values

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
    DEBUG = values.BooleanValue(default=False)

    AUTH_USER_MODEL = "users.UserModel"
    WSGI_APPLICATION = "wsgi.application"

    @property
    def BASE_DIR(self) -> str:  # noqa: N802
        # Get /app/settings/common/base.py and get 2 parent for /app response
        base_dir = Path(__file__).parents[2]

        # Add apps as PYTHONPATH
        base_app_dir: str = str(base_dir / "apps")
        sys.path.append(base_app_dir)

        # Add IAM as PYTHONPATH
        base_app_iam: str = str(base_dir / "apps" / "iam")
        sys.path.append(base_app_iam)

        return str(base_dir)
