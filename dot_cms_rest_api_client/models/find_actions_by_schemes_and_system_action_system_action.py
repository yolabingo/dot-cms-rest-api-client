from enum import Enum


class FindActionsBySchemesAndSystemActionSystemAction(str, Enum):
    NEW = "NEW"
    EDIT = "EDIT"
    PUBLISH = "PUBLISH"
    UNPUBLISH = "UNPUBLISH"
    ARCHIVE = "ARCHIVE"
    UNARCHIVE = "UNARCHIVE"
    DELETE = "DELETE"
    DESTROY = "DESTROY"

    def __str__(self) -> str:
        return str(self.value)
