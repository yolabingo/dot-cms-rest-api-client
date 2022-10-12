from enum import Enum


class WorkflowActionShowOnItem(str, Enum):
    NEW = "NEW"
    LOCKED = "LOCKED"
    UNLOCKED = "UNLOCKED"
    PUBLISHED = "PUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"
    ARCHIVED = "ARCHIVED"
    LISTING = "LISTING"
    EDITING = "EDITING"

    def __str__(self) -> str:
        return str(self.value)
