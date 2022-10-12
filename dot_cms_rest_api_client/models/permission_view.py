from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.permission_view_permission import PermissionViewPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="PermissionView")


@attr.s(auto_attribs=True)
class PermissionView:
    """
    Attributes:
        id (Union[Unset, int]):
        inode (Union[Unset, str]):
        role_id (Union[Unset, str]):
        permission (Union[Unset, PermissionViewPermission]):
        type (Union[Unset, str]):
        bit_permission (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    inode: Union[Unset, str] = UNSET
    role_id: Union[Unset, str] = UNSET
    permission: Union[Unset, PermissionViewPermission] = UNSET
    type: Union[Unset, str] = UNSET
    bit_permission: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        inode = self.inode
        role_id = self.role_id
        permission: Union[Unset, str] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        type = self.type
        bit_permission = self.bit_permission

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if inode is not UNSET:
            field_dict["inode"] = inode
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if permission is not UNSET:
            field_dict["permission"] = permission
        if type is not UNSET:
            field_dict["type"] = type
        if bit_permission is not UNSET:
            field_dict["bitPermission"] = bit_permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        inode = d.pop("inode", UNSET)

        role_id = d.pop("roleId", UNSET)

        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, PermissionViewPermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = PermissionViewPermission(_permission)

        type = d.pop("type", UNSET)

        bit_permission = d.pop("bitPermission", UNSET)

        permission_view = cls(
            id=id,
            inode=inode,
            role_id=role_id,
            permission=permission,
            type=type,
            bit_permission=bit_permission,
        )

        permission_view.additional_properties = d
        return permission_view

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
