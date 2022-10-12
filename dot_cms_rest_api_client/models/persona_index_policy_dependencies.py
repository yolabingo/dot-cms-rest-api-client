from enum import Enum


class PersonaIndexPolicyDependencies(str, Enum):
    DEFER = "DEFER"
    WAIT_FOR = "WAIT_FOR"
    FORCE = "FORCE"

    def __str__(self) -> str:
        return str(self.value)
