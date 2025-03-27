from __future__ import annotations


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
        return self.get_local_apps()

    @property
    def DJANGO_APPS(self) -> list[str]:  # noqa: N802
        django_top = self.get_django_apps_t()
        django_bottom = self.get_django_apps_b()
        return [
            *django_top,
            *django_bottom,
        ]

    @property
    def THIRD_PARTY_APPS(self) -> list[str]:  # noqa: N802
        tparty_apps = self.get_third_party_apps()
        return ["anymail", *tparty_apps]

    @property
    def COMMON_APPS(self) -> list[str]:  # noqa: N802
        return [
            "users",
        ]

    @property
    def INSTALLED_APPS(self) -> list[str]:  # noqa: N802
        return self.COMMON_APPS + self.DJANGO_APPS + self.LOCAL_APPS + self.THIRD_PARTY_APPS
