import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.form_data_content_disposition import FormDataContentDisposition
from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveCompanyLogoMultipartData")


@attr.s(auto_attribs=True)
class SaveCompanyLogoMultipartData:
    """
    Attributes:
        user (Union[Unset, str]):
        password (Union[Unset, str]):
        logo_file (Union[Unset, FormDataContentDisposition]):
    """

    user: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    logo_file: Union[Unset, FormDataContentDisposition] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user
        password = self.password
        logo_file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.logo_file, Unset):
            logo_file = self.logo_file.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if password is not UNSET:
            field_dict["password"] = password
        if logo_file is not UNSET:
            field_dict["logoFile"] = logo_file

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        password = (
            self.password if isinstance(self.password, Unset) else (None, str(self.password).encode(), "text/plain")
        )
        logo_file: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.logo_file, Unset):
            logo_file = (None, json.dumps(self.logo_file.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if password is not UNSET:
            field_dict["password"] = password
        if logo_file is not UNSET:
            field_dict["logoFile"] = logo_file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user", UNSET)

        password = d.pop("password", UNSET)

        _logo_file = d.pop("logoFile", UNSET)
        logo_file: Union[Unset, FormDataContentDisposition]
        if isinstance(_logo_file, Unset):
            logo_file = UNSET
        else:
            logo_file = FormDataContentDisposition.from_dict(_logo_file)

        save_company_logo_multipart_data = cls(
            user=user,
            password=password,
            logo_file=logo_file,
        )

        save_company_logo_multipart_data.additional_properties = d
        return save_company_logo_multipart_data

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
