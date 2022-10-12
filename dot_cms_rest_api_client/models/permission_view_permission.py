from enum import Enum


class PermissionViewPermission(str, Enum):
    READ = "READ"
    USE = "USE"
    EDIT = "EDIT"
    WRITE = "WRITE"
    PUBLISH = "PUBLISH"
    EDIT_PERMISSIONS = "EDIT_PERMISSIONS"
    CAN_ADD_CHILDREN = "CAN_ADD_CHILDREN"

    def __str__(self) -> str:
        return str(self.value)
