# Third Party Stuff
from __future__ import annotations


class BaseURLConfig:
    ROOT_URLCONF: str = "urls.admin"


class BaseStaticFilesConfig:
    STATIC_URL: str = "static/"


class BaseInternationalizationConfig:
    LANGUAGE_CODE: str = "es-MX"
    TIME_ZONE: str = "America/Mexico_City"
    USE_I18N: bool = True
    USE_TZ: bool = True


class BaseMiddlewareConfig:
    def get_middleware_t(self) -> list:
        return []

    def get_middleware_b(self) -> list:
        return []

    @property
    def MIDDLEWARE(self) -> list[str]:  # noqa: N802
        middleware_top = self.get_middleware_t()
        middleware_bottom = self.get_middleware_b()
        return [
            *middleware_top,
            "django.middleware.locale.LocaleMiddleware",
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
            "django_structlog.middlewares.RequestMiddleware",
            "whitenoise.middleware.WhiteNoiseMiddleware",  # Statics
            "debug_toolbar.middleware.DebugToolbarMiddleware",
            *middleware_bottom,
        ]


class BaseTemplateConfig:
    @property
    def TEMPLATES(self) -> list[dict]:  # noqa: N802
        return [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        "django.template.context_processors.debug",
                        "django.template.context_processors.request",
                        "django.contrib.auth.context_processors.auth",
                        "django.contrib.messages.context_processors.messages",
                    ],
                },
            },
        ]
