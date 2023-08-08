# Standard Library
import os


class BaseMailConfig:
    EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
    ANYMAIL = {"SENDGRID_API_KEY": os.getenv("SENDGRID_API_KEY")}  # noqa: F405
