from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestConditionValue")


@attr.s(auto_attribs=True)
class RestConditionValue:
    """
    Attributes:
        key (str):
        value (Union[Unset, str]):
        priority (Union[Unset, int]):
    """

    key: str
    value: Union[Unset, str] = UNSET
    priority: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        value = self.value
        priority = self.priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        value = d.pop("value", UNSET)

        priority = d.pop("priority", UNSET)

        rest_condition_value = cls(
            key=key,
            value=value,
            priority=priority,
        )

        rest_condition_value.additional_properties = d
        return rest_condition_value

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
