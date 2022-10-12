from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanguageForm")


@attr.s(auto_attribs=True)
class LanguageForm:
    """
    Attributes:
        language_code (Union[Unset, str]):
        country_code (Union[Unset, str]):
        language (Union[Unset, str]):
        country (Union[Unset, str]):
    """

    language_code: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language_code = self.language_code
        country_code = self.country_code
        language = self.language
        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if language is not UNSET:
            field_dict["language"] = language
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language_code = d.pop("languageCode", UNSET)

        country_code = d.pop("countryCode", UNSET)

        language = d.pop("language", UNSET)

        country = d.pop("country", UNSET)

        language_form = cls(
            language_code=language_code,
            country_code=country_code,
            language=language,
            country=country,
        )

        language_form.additional_properties = d
        return language_form

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
