from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="I18NForm")


@attr.s(auto_attribs=True)
class I18NForm:
    """
    Attributes:
        language (Union[Unset, str]):
        country (Union[Unset, str]):
        messages_key (Union[Unset, List[str]]):
    """

    language: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    messages_key: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        country = self.country
        messages_key: Union[Unset, List[str]] = UNSET
        if not isinstance(self.messages_key, Unset):
            messages_key = self.messages_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if country is not UNSET:
            field_dict["country"] = country
        if messages_key is not UNSET:
            field_dict["messagesKey"] = messages_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language", UNSET)

        country = d.pop("country", UNSET)

        messages_key = cast(List[str], d.pop("messagesKey", UNSET))

        i18n_form = cls(
            language=language,
            country=country,
            messages_key=messages_key,
        )

        i18n_form.additional_properties = d
        return i18n_form

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
