from __future__ import annotations


class AdminInterfaceConfig:
    X_FRAME_OPTIONS: str = "SAMEORIGIN"

    @property
    def SILENCED_SYSTEM_CHECKS(self) -> list[str]:  # noqa: N802
        return [
            "security.W019",
        ]
