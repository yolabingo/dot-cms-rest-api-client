from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Permission")


@attr.s(auto_attribs=True)
class Permission:
    """
    Attributes:
        id (Union[Unset, int]):
        inode (Union[Unset, str]):
        permission (Union[Unset, int]):
        type (Union[Unset, str]):
        bit_permission (Union[Unset, bool]):
        individual_permission (Union[Unset, bool]):
        role_id (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    inode: Union[Unset, str] = UNSET
    permission: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    bit_permission: Union[Unset, bool] = UNSET
    individual_permission: Union[Unset, bool] = UNSET
    role_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        inode = self.inode
        permission = self.permission
        type = self.type
        bit_permission = self.bit_permission
        individual_permission = self.individual_permission
        role_id = self.role_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if inode is not UNSET:
            field_dict["inode"] = inode
        if permission is not UNSET:
            field_dict["permission"] = permission
        if type is not UNSET:
            field_dict["type"] = type
        if bit_permission is not UNSET:
            field_dict["bitPermission"] = bit_permission
        if individual_permission is not UNSET:
            field_dict["individualPermission"] = individual_permission
        if role_id is not UNSET:
            field_dict["roleId"] = role_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        inode = d.pop("inode", UNSET)

        permission = d.pop("permission", UNSET)

        type = d.pop("type", UNSET)

        bit_permission = d.pop("bitPermission", UNSET)

        individual_permission = d.pop("individualPermission", UNSET)

        role_id = d.pop("roleId", UNSET)

        permission = cls(
            id=id,
            inode=inode,
            permission=permission,
            type=type,
            bit_permission=bit_permission,
            individual_permission=individual_permission,
            role_id=role_id,
        )

        permission.additional_properties = d
        return permission

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
