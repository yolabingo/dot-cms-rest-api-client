from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTokenForm")


@attr.s(auto_attribs=True)
class CreateTokenForm:
    """
    Attributes:
        user (str):
        password (str):
        expiration_days (Union[Unset, int]):
        label (Union[Unset, str]):
    """

    user: str
    password: str
    expiration_days: Union[Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user
        password = self.password
        expiration_days = self.expiration_days
        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "password": password,
            }
        )
        if expiration_days is not UNSET:
            field_dict["expirationDays"] = expiration_days
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user")

        password = d.pop("password")

        expiration_days = d.pop("expirationDays", UNSET)

        label = d.pop("label", UNSET)

        create_token_form = cls(
            user=user,
            password=password,
            expiration_days=expiration_days,
            label=label,
        )

        create_token_form.additional_properties = d
        return create_token_form

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
