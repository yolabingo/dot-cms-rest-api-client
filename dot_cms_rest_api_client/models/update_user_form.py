from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserForm")


@attr.s(auto_attribs=True)
class UpdateUserForm:
    """
    Attributes:
        user_id (str):
        given_name (str):
        surname (str):
        email (Union[Unset, str]):
        current_password (Union[Unset, str]):
        new_password (Union[Unset, str]):
    """

    user_id: str
    given_name: str
    surname: str
    email: Union[Unset, str] = UNSET
    current_password: Union[Unset, str] = UNSET
    new_password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        given_name = self.given_name
        surname = self.surname
        email = self.email
        current_password = self.current_password
        new_password = self.new_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "givenName": given_name,
                "surname": surname,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if current_password is not UNSET:
            field_dict["currentPassword"] = current_password
        if new_password is not UNSET:
            field_dict["newPassword"] = new_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        given_name = d.pop("givenName")

        surname = d.pop("surname")

        email = d.pop("email", UNSET)

        current_password = d.pop("currentPassword", UNSET)

        new_password = d.pop("newPassword", UNSET)

        update_user_form = cls(
            user_id=user_id,
            given_name=given_name,
            surname=surname,
            email=email,
            current_password=current_password,
            new_password=new_password,
        )

        update_user_form.additional_properties = d
        return update_user_form

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
