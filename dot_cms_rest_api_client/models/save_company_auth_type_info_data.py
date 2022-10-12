from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveCompanyAuthTypeInfoData")


@attr.s(auto_attribs=True)
class SaveCompanyAuthTypeInfoData:
    """
    Attributes:
        user (Union[Unset, str]):
        password (Union[Unset, str]):
        auth_type (Union[Unset, str]):
    """

    user: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    auth_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user
        password = self.password
        auth_type = self.auth_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if password is not UNSET:
            field_dict["password"] = password
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user", UNSET)

        password = d.pop("password", UNSET)

        auth_type = d.pop("authType", UNSET)

        save_company_auth_type_info_data = cls(
            user=user,
            password=password,
            auth_type=auth_type,
        )

        save_company_auth_type_info_data.additional_properties = d
        return save_company_auth_type_info_data

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
