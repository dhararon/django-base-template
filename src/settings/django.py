# Third Party Stuff
from configurations import Configuration


class BaseURLConfig:
    ROOT_URLCONF = "urls.admin"


class BaseStaticFilesConfig:
    STATIC_URL = "static/"


class BaseInternationalizationConfig:
    LANGUAGE_CODE = "es-mx"
    TIME_ZONE = "America/Mexico_City"
    USE_I18N = True
    USE_TZ = True


class BaseMiddlewareConfig:
    MIDDLEWARE = Configuration.MIDDLEWARE + [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",  # Statics
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "django_structlog.middlewares.RequestMiddleware",
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]


class BaseTemplateConfig:
    @property
    def TEMPLATES(self):
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
