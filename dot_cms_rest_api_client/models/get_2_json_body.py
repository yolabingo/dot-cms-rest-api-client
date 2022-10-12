from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.get_2_json_body_additional_property import Get2JsonBodyAdditionalProperty

T = TypeVar("T", bound="Get2JsonBody")


@attr.s(auto_attribs=True)
class Get2JsonBody:
    """ """

    additional_properties: Dict[str, Get2JsonBodyAdditionalProperty] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_2_json_body = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Get2JsonBodyAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_2_json_body.additional_properties = additional_properties
        return get_2_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Get2JsonBodyAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Get2JsonBodyAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
