from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user import User
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAPI")


@attr.s(auto_attribs=True)
class UserAPI:
    """
    Attributes:
        anonymous_user (Union[Unset, User]):
        system_user (Union[Unset, User]):
        un_deleted_users (Union[Unset, List[User]]):
        default_user (Union[Unset, User]):
        anonymous_user_no_throw (Union[Unset, User]):
    """

    anonymous_user: Union[Unset, User] = UNSET
    system_user: Union[Unset, User] = UNSET
    un_deleted_users: Union[Unset, List[User]] = UNSET
    default_user: Union[Unset, User] = UNSET
    anonymous_user_no_throw: Union[Unset, User] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        anonymous_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.anonymous_user, Unset):
            anonymous_user = self.anonymous_user.to_dict()

        system_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.system_user, Unset):
            system_user = self.system_user.to_dict()

        un_deleted_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.un_deleted_users, Unset):
            un_deleted_users = []
            for un_deleted_users_item_data in self.un_deleted_users:
                un_deleted_users_item = un_deleted_users_item_data.to_dict()

                un_deleted_users.append(un_deleted_users_item)

        default_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_user, Unset):
            default_user = self.default_user.to_dict()

        anonymous_user_no_throw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.anonymous_user_no_throw, Unset):
            anonymous_user_no_throw = self.anonymous_user_no_throw.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anonymous_user is not UNSET:
            field_dict["anonymousUser"] = anonymous_user
        if system_user is not UNSET:
            field_dict["systemUser"] = system_user
        if un_deleted_users is not UNSET:
            field_dict["unDeletedUsers"] = un_deleted_users
        if default_user is not UNSET:
            field_dict["defaultUser"] = default_user
        if anonymous_user_no_throw is not UNSET:
            field_dict["anonymousUserNoThrow"] = anonymous_user_no_throw

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _anonymous_user = d.pop("anonymousUser", UNSET)
        anonymous_user: Union[Unset, User]
        if isinstance(_anonymous_user, Unset):
            anonymous_user = UNSET
        else:
            anonymous_user = User.from_dict(_anonymous_user)

        _system_user = d.pop("systemUser", UNSET)
        system_user: Union[Unset, User]
        if isinstance(_system_user, Unset):
            system_user = UNSET
        else:
            system_user = User.from_dict(_system_user)

        un_deleted_users = []
        _un_deleted_users = d.pop("unDeletedUsers", UNSET)
        for un_deleted_users_item_data in _un_deleted_users or []:
            un_deleted_users_item = User.from_dict(un_deleted_users_item_data)

            un_deleted_users.append(un_deleted_users_item)

        _default_user = d.pop("defaultUser", UNSET)
        default_user: Union[Unset, User]
        if isinstance(_default_user, Unset):
            default_user = UNSET
        else:
            default_user = User.from_dict(_default_user)

        _anonymous_user_no_throw = d.pop("anonymousUserNoThrow", UNSET)
        anonymous_user_no_throw: Union[Unset, User]
        if isinstance(_anonymous_user_no_throw, Unset):
            anonymous_user_no_throw = UNSET
        else:
            anonymous_user_no_throw = User.from_dict(_anonymous_user_no_throw)

        user_api = cls(
            anonymous_user=anonymous_user,
            system_user=system_user,
            un_deleted_users=un_deleted_users,
            default_user=default_user,
            anonymous_user_no_throw=anonymous_user_no_throw,
        )

        user_api.additional_properties = d
        return user_api

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
