from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.set_form_value import SetFormValue

T = TypeVar("T", bound="SetForm")


@attr.s(auto_attribs=True)
class SetForm:
    """
    Attributes:
        key (str):
        value (SetFormValue):
    """

    key: str
    value: SetFormValue
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        value = SetFormValue.from_dict(d.pop("value"))

        set_form = cls(
            key=key,
            value=value,
        )

        set_form.additional_properties = d
        return set_form

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
