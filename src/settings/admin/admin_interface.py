from typing import ClassVar


class AdminInterfaceConfig:
    X_FRAME_OPTIONS: str = "SAMEORIGIN"
    SILENCED_SYSTEM_CHECKS: ClassVar[list] = ["security.W019"]
