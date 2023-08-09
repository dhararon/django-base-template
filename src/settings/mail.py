import os
from typing import ClassVar


class BaseMailConfig:
    EMAIL_BACKEND: str = "anymail.backends.sendgrid.EmailBackend"
    ANYMAIL: ClassVar[dict] = {"SENDGRID_API_KEY": os.getenv("SENDGRID_API_KEY")}
