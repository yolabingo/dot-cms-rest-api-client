from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParameterModel")


@attr.s(auto_attribs=True)
class ParameterModel:
    """
    Attributes:
        id (Union[Unset, str]):
        owner_id (Union[Unset, str]):
        key (Union[Unset, str]):
        value (Union[Unset, str]):
        priority (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    priority: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        owner_id = self.owner_id
        key = self.key
        value = self.value
        priority = self.priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        priority = d.pop("priority", UNSET)

        parameter_model = cls(
            id=id,
            owner_id=owner_id,
            key=key,
            value=value,
            priority=priority,
        )

        parameter_model.additional_properties = d
        return parameter_model

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
