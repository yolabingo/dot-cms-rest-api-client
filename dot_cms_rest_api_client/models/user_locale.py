from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserLocale")


@attr.s(auto_attribs=True)
class UserLocale:
    """
    Attributes:
        display_name (Union[Unset, str]):
        script (Union[Unset, str]):
        country (Union[Unset, str]):
        variant (Union[Unset, str]):
        extension_keys (Union[Unset, List[str]]):
        unicode_locale_attributes (Union[Unset, List[str]]):
        unicode_locale_keys (Union[Unset, List[str]]):
        iso_3_language (Union[Unset, str]):
        iso_3_country (Union[Unset, str]):
        display_language (Union[Unset, str]):
        display_script (Union[Unset, str]):
        display_country (Union[Unset, str]):
        display_variant (Union[Unset, str]):
        language (Union[Unset, str]):
    """

    display_name: Union[Unset, str] = UNSET
    script: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    variant: Union[Unset, str] = UNSET
    extension_keys: Union[Unset, List[str]] = UNSET
    unicode_locale_attributes: Union[Unset, List[str]] = UNSET
    unicode_locale_keys: Union[Unset, List[str]] = UNSET
    iso_3_language: Union[Unset, str] = UNSET
    iso_3_country: Union[Unset, str] = UNSET
    display_language: Union[Unset, str] = UNSET
    display_script: Union[Unset, str] = UNSET
    display_country: Union[Unset, str] = UNSET
    display_variant: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        script = self.script
        country = self.country
        variant = self.variant
        extension_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.extension_keys, Unset):
            extension_keys = self.extension_keys

        unicode_locale_attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.unicode_locale_attributes, Unset):
            unicode_locale_attributes = self.unicode_locale_attributes

        unicode_locale_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.unicode_locale_keys, Unset):
            unicode_locale_keys = self.unicode_locale_keys

        iso_3_language = self.iso_3_language
        iso_3_country = self.iso_3_country
        display_language = self.display_language
        display_script = self.display_script
        display_country = self.display_country
        display_variant = self.display_variant
        language = self.language

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if script is not UNSET:
            field_dict["script"] = script
        if country is not UNSET:
            field_dict["country"] = country
        if variant is not UNSET:
            field_dict["variant"] = variant
        if extension_keys is not UNSET:
            field_dict["extensionKeys"] = extension_keys
        if unicode_locale_attributes is not UNSET:
            field_dict["unicodeLocaleAttributes"] = unicode_locale_attributes
        if unicode_locale_keys is not UNSET:
            field_dict["unicodeLocaleKeys"] = unicode_locale_keys
        if iso_3_language is not UNSET:
            field_dict["iso3Language"] = iso_3_language
        if iso_3_country is not UNSET:
            field_dict["iso3Country"] = iso_3_country
        if display_language is not UNSET:
            field_dict["displayLanguage"] = display_language
        if display_script is not UNSET:
            field_dict["displayScript"] = display_script
        if display_country is not UNSET:
            field_dict["displayCountry"] = display_country
        if display_variant is not UNSET:
            field_dict["displayVariant"] = display_variant
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        script = d.pop("script", UNSET)

        country = d.pop("country", UNSET)

        variant = d.pop("variant", UNSET)

        extension_keys = cast(List[str], d.pop("extensionKeys", UNSET))

        unicode_locale_attributes = cast(List[str], d.pop("unicodeLocaleAttributes", UNSET))

        unicode_locale_keys = cast(List[str], d.pop("unicodeLocaleKeys", UNSET))

        iso_3_language = d.pop("iso3Language", UNSET)

        iso_3_country = d.pop("iso3Country", UNSET)

        display_language = d.pop("displayLanguage", UNSET)

        display_script = d.pop("displayScript", UNSET)

        display_country = d.pop("displayCountry", UNSET)

        display_variant = d.pop("displayVariant", UNSET)

        language = d.pop("language", UNSET)

        user_locale = cls(
            display_name=display_name,
            script=script,
            country=country,
            variant=variant,
            extension_keys=extension_keys,
            unicode_locale_attributes=unicode_locale_attributes,
            unicode_locale_keys=unicode_locale_keys,
            iso_3_language=iso_3_language,
            iso_3_country=iso_3_country,
            display_language=display_language,
            display_script=display_script,
            display_country=display_country,
            display_variant=display_variant,
            language=language,
        )

        user_locale.additional_properties = d
        return user_locale

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
