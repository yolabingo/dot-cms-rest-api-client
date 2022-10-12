from enum import Enum


class GenerateBundleFormOperation(str, Enum):
    PUBLISH = "PUBLISH"
    UNPUBLISH = "UNPUBLISH"

    def __str__(self) -> str:
        return str(self.value)
