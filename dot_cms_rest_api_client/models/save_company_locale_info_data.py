from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveCompanyLocaleInfoData")


@attr.s(auto_attribs=True)
class SaveCompanyLocaleInfoData:
    """
    Attributes:
        user (Union[Unset, str]):
        password (Union[Unset, str]):
        language_id (Union[Unset, str]):
        time_zone_id (Union[Unset, str]):
    """

    user: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    language_id: Union[Unset, str] = UNSET
    time_zone_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user
        password = self.password
        language_id = self.language_id
        time_zone_id = self.time_zone_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if password is not UNSET:
            field_dict["password"] = password
        if language_id is not UNSET:
            field_dict["languageId"] = language_id
        if time_zone_id is not UNSET:
            field_dict["timeZoneId"] = time_zone_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user", UNSET)

        password = d.pop("password", UNSET)

        language_id = d.pop("languageId", UNSET)

        time_zone_id = d.pop("timeZoneId", UNSET)

        save_company_locale_info_data = cls(
            user=user,
            password=password,
            language_id=language_id,
            time_zone_id=time_zone_id,
        )

        save_company_locale_info_data.additional_properties = d
        return save_company_locale_info_data

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
