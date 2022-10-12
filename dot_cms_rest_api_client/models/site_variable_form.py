from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteVariableForm")


@attr.s(auto_attribs=True)
class SiteVariableForm:
    """
    Attributes:
        id (Union[Unset, str]):
        site_id (Union[Unset, str]):
        name (Union[Unset, str]):
        key (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        site_id = self.site_id
        name = self.name
        key = self.key
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if name is not UNSET:
            field_dict["name"] = name
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        site_id = d.pop("siteId", UNSET)

        name = d.pop("name", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        site_variable_form = cls(
            id=id,
            site_id=site_id,
            name=name,
            key=key,
            value=value,
        )

        site_variable_form.additional_properties = d
        return site_variable_form

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
