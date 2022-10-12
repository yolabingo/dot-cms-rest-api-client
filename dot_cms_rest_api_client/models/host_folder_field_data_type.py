from enum import Enum


class HostFolderFieldDataType(str, Enum):
    NONE = "none"
    BOOL = "bool"
    DATE = "date"
    FLOAT = "float"
    INTEGER = "integer"
    TEXT = "text"
    TEXT_AREA = "text_area"
    SYSTEM_FIELD = "system_field"

    def __str__(self) -> str:
        return str(self.value)
