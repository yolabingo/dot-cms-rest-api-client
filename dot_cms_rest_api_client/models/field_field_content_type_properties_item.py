from enum import Enum


class FieldFieldContentTypePropertiesItem(str, Enum):
    NAME = "NAME"
    VALUES = "VALUES"
    CATEGORIES = "CATEGORIES"
    RELATIONSHIPS = "RELATIONSHIPS"
    REGEX_CHECK = "REGEX_CHECK"
    HINT = "HINT"
    REQUIRED = "REQUIRED"
    SEARCHABLE = "SEARCHABLE"
    INDEXED = "INDEXED"
    LISTED = "LISTED"
    UNIQUE = "UNIQUE"
    DEFAULT_VALUE = "DEFAULT_VALUE"
    DATA_TYPE = "DATA_TYPE"

    def __str__(self) -> str:
        return str(self.value)
