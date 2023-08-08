from .dev import DevConfig


class LocalConfig(DevConfig):
    def get_django_apps_b(self):
        return [
            "django_extensions",
        ]
