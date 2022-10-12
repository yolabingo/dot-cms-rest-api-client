from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestUser")


@attr.s(auto_attribs=True)
class RestUser:
    """
    Attributes:
        user_id (Union[Unset, str]):
        given_name (Union[Unset, str]):
        email (Union[Unset, str]):
        surname (Union[Unset, str]):
        role_id (Union[Unset, str]):
        login_as (Union[Unset, bool]):
    """

    user_id: Union[Unset, str] = UNSET
    given_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    role_id: Union[Unset, str] = UNSET
    login_as: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        given_name = self.given_name
        email = self.email
        surname = self.surname
        role_id = self.role_id
        login_as = self.login_as

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if email is not UNSET:
            field_dict["email"] = email
        if surname is not UNSET:
            field_dict["surname"] = surname
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if login_as is not UNSET:
            field_dict["loginAs"] = login_as

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId", UNSET)

        given_name = d.pop("givenName", UNSET)

        email = d.pop("email", UNSET)

        surname = d.pop("surname", UNSET)

        role_id = d.pop("roleId", UNSET)

        login_as = d.pop("loginAs", UNSET)

        rest_user = cls(
            user_id=user_id,
            given_name=given_name,
            email=email,
            surname=surname,
            role_id=role_id,
            login_as=login_as,
        )

        rest_user.additional_properties = d
        return rest_user

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
