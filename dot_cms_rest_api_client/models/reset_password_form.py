from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ResetPasswordForm")


@attr.s(auto_attribs=True)
class ResetPasswordForm:
    """
    Attributes:
        token (str):
        password (str):
    """

    token: str
    password: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        password = d.pop("password")

        reset_password_form = cls(
            token=token,
            password=password,
        )

        reset_password_form.additional_properties = d
        return reset_password_form

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
