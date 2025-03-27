from configurations import values


class BaseDatabaseConfig:
    @property
    def DATABASES(self) -> dict:  # noqa: N802
        pg_db: str = values.Value(environ_name="POSTGRES_DB", environ_prefix=None)
        pg_user: str = values.Value(environ_name="POSTGRES_USER", environ_prefix=None)
        pg_pwd: str = values.Value(environ_name="POSTGRES_PASSWORD", environ_prefix=None)
        pg_host: str = values.Value(environ_name="POSTGRES_HOST", environ_prefix=None)
        pg_port: str = values.Value(environ_name="POSTGRES_PORT", environ_prefix=None)

        return {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": pg_db,
                "USER": pg_user,
                "PASSWORD": pg_pwd,
                "HOST": pg_host,
                "PORT": pg_port,
                "ATOMIC_REQUESTS": True,
            },
        }
