from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmallRoleView")


@attr.s(auto_attribs=True)
class SmallRoleView:
    """
    Attributes:
        name (Union[Unset, str]):
        id (Union[Unset, str]):
        role_key (Union[Unset, str]):
        user (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    role_key: Union[Unset, str] = UNSET
    user: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        role_key = self.role_key
        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if role_key is not UNSET:
            field_dict["roleKey"] = role_key
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        role_key = d.pop("roleKey", UNSET)

        user = d.pop("user", UNSET)

        small_role_view = cls(
            name=name,
            id=id,
            role_key=role_key,
            user=user,
        )

        small_role_view.additional_properties = d
        return small_role_view

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
