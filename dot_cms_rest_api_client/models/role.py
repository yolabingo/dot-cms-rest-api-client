from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Role")


@attr.s(auto_attribs=True)
class Role:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        role_key (Union[Unset, str]):
        parent (Union[Unset, str]):
        edit_permissions (Union[Unset, bool]):
        edit_users (Union[Unset, bool]):
        edit_layouts (Union[Unset, bool]):
        locked (Union[Unset, bool]):
        system (Union[Unset, bool]):
        role_children (Union[Unset, List[str]]):
        fqn (Union[Unset, str]):
        dbfqn (Union[Unset, str]):
        user (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    role_key: Union[Unset, str] = UNSET
    parent: Union[Unset, str] = UNSET
    edit_permissions: Union[Unset, bool] = UNSET
    edit_users: Union[Unset, bool] = UNSET
    edit_layouts: Union[Unset, bool] = UNSET
    locked: Union[Unset, bool] = UNSET
    system: Union[Unset, bool] = UNSET
    role_children: Union[Unset, List[str]] = UNSET
    fqn: Union[Unset, str] = UNSET
    dbfqn: Union[Unset, str] = UNSET
    user: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        role_key = self.role_key
        parent = self.parent
        edit_permissions = self.edit_permissions
        edit_users = self.edit_users
        edit_layouts = self.edit_layouts
        locked = self.locked
        system = self.system
        role_children: Union[Unset, List[str]] = UNSET
        if not isinstance(self.role_children, Unset):
            role_children = self.role_children

        fqn = self.fqn
        dbfqn = self.dbfqn
        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if role_key is not UNSET:
            field_dict["roleKey"] = role_key
        if parent is not UNSET:
            field_dict["parent"] = parent
        if edit_permissions is not UNSET:
            field_dict["editPermissions"] = edit_permissions
        if edit_users is not UNSET:
            field_dict["editUsers"] = edit_users
        if edit_layouts is not UNSET:
            field_dict["editLayouts"] = edit_layouts
        if locked is not UNSET:
            field_dict["locked"] = locked
        if system is not UNSET:
            field_dict["system"] = system
        if role_children is not UNSET:
            field_dict["roleChildren"] = role_children
        if fqn is not UNSET:
            field_dict["fqn"] = fqn
        if dbfqn is not UNSET:
            field_dict["dbfqn"] = dbfqn
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        role_key = d.pop("roleKey", UNSET)

        parent = d.pop("parent", UNSET)

        edit_permissions = d.pop("editPermissions", UNSET)

        edit_users = d.pop("editUsers", UNSET)

        edit_layouts = d.pop("editLayouts", UNSET)

        locked = d.pop("locked", UNSET)

        system = d.pop("system", UNSET)

        role_children = cast(List[str], d.pop("roleChildren", UNSET))

        fqn = d.pop("fqn", UNSET)

        dbfqn = d.pop("dbfqn", UNSET)

        user = d.pop("user", UNSET)

        role = cls(
            id=id,
            name=name,
            description=description,
            role_key=role_key,
            parent=parent,
            edit_permissions=edit_permissions,
            edit_users=edit_users,
            edit_layouts=edit_layouts,
            locked=locked,
            system=system,
            role_children=role_children,
            fqn=fqn,
            dbfqn=dbfqn,
            user=user,
        )

        role.additional_properties = d
        return role

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
