from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleLayoutForm")


@attr.s(auto_attribs=True)
class RoleLayoutForm:
    """
    Attributes:
        role_id (Union[Unset, str]):
        layout_ids (Union[Unset, List[str]]):
    """

    role_id: Union[Unset, str] = UNSET
    layout_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role_id = self.role_id
        layout_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.layout_ids, Unset):
            layout_ids = self.layout_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if layout_ids is not UNSET:
            field_dict["layoutIds"] = layout_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role_id = d.pop("roleId", UNSET)

        layout_ids = cast(List[str], d.pop("layoutIds", UNSET))

        role_layout_form = cls(
            role_id=role_id,
            layout_ids=layout_ids,
        )

        role_layout_form.additional_properties = d
        return role_layout_form

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
