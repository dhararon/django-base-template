from __future__ import annotations

import socket

from settings.api.env_dev import DevConfig


class LocalConfig(DevConfig):
    @property
    def INTERNAL_IPS(self) -> list[str]:  # noqa: N802
        # Standard Library
        hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
        return [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
