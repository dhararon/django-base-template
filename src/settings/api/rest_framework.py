from typing import ClassVar


class BaseRestFrameworkConfig:
    REST_FRAMEWORK: ClassVar[dict] = {
        "DEFAULT_RENDERER_CLASSES": [
            "rest_framework.renderers.JSONRenderer",
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": ["knox.auth.TokenAuthentication"],
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.IsAuthenticated",
        ],
        "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    }


class BaseSpectacularConfig:
    SPECTACULAR_SETTINGS: ClassVar[dict] = {
        "TITLE": "template",
        "DESCRIPTION": "",
        "VERSION": "1.0.0",
        "SERVE_INCLUDE_SCHEMA": False,
    }
