from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationForm")


@attr.s(auto_attribs=True)
class AuthenticationForm:
    """
    Attributes:
        user_id (str):
        password (str):
        remember_me (Union[Unset, bool]):
        back_end_login (Union[Unset, bool]):
        language (Union[Unset, str]):
        country (Union[Unset, str]):
    """

    user_id: str
    password: str
    remember_me: Union[Unset, bool] = UNSET
    back_end_login: Union[Unset, bool] = UNSET
    language: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        password = self.password
        remember_me = self.remember_me
        back_end_login = self.back_end_login
        language = self.language
        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "password": password,
            }
        )
        if remember_me is not UNSET:
            field_dict["rememberMe"] = remember_me
        if back_end_login is not UNSET:
            field_dict["backEndLogin"] = back_end_login
        if language is not UNSET:
            field_dict["language"] = language
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        password = d.pop("password")

        remember_me = d.pop("rememberMe", UNSET)

        back_end_login = d.pop("backEndLogin", UNSET)

        language = d.pop("language", UNSET)

        country = d.pop("country", UNSET)

        authentication_form = cls(
            user_id=user_id,
            password=password,
            remember_me=remember_me,
            back_end_login=back_end_login,
            language=language,
            country=country,
        )

        authentication_form.additional_properties = d
        return authentication_form

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
