# Third Party Stuff
pass


class BaseAppConfig:
    def get_local_apps(self) -> list:
        return []

    def get_django_apps_t(self) -> list:
        return []

    def get_django_apps_b(self) -> list:
        return []

    def get_third_party_apps(self) -> list:
        return []

    @property
    def LOCAL_APPS(self) -> list:  # noqa: N802
        local_apps = self.get_local_apps()
        return ["apps.users", *local_apps]

    @property
    def DJANGO_APPS(self):  # noqa: N802
        django_top = self.get_django_apps_t()
        django_bottom = self.get_django_apps_b()
        return [
            *django_top,
            "admin_interface",
            "colorfield",
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            *django_bottom,
        ]

    @property
    def THIRD_PARTY_APPS(self):  # noqa: N802
        tparty_apps = self.get_third_party_apps()
        return ["anymail", *tparty_apps]

    @property
    def INSTALLED_APPS(self):  # noqa: N802
        return self.LOCAL_APPS + self.DJANGO_APPS + self.THIRD_PARTY_APPS
