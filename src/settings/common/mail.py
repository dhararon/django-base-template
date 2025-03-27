from configurations import values


class BaseMailConfig:
    EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"

    @property
    def ANYMAIL(self) -> dict:  # noqa: N802
        sendgrid_api_key: str = values.Value(environ_name="SENDGRID_API_KEY")
        return {
            "SENDGRID_API_KEY": sendgrid_api_key,
        }
