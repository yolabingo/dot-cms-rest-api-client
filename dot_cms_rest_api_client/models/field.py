from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.field_field_content_type_properties_item import FieldFieldContentTypePropertiesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Field")


@attr.s(auto_attribs=True)
class Field:
    """
    Attributes:
        clazz (str):
        field_content_type_properties (Union[Unset, List[FieldFieldContentTypePropertiesItem]]):
    """

    clazz: str
    field_content_type_properties: Union[Unset, List[FieldFieldContentTypePropertiesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clazz = self.clazz
        field_content_type_properties: Union[Unset, List[str]] = UNSET
        if not isinstance(self.field_content_type_properties, Unset):
            field_content_type_properties = []
            for field_content_type_properties_item_data in self.field_content_type_properties:
                field_content_type_properties_item = field_content_type_properties_item_data.value

                field_content_type_properties.append(field_content_type_properties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clazz": clazz,
            }
        )
        if field_content_type_properties is not UNSET:
            field_dict["fieldContentTypeProperties"] = field_content_type_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clazz = d.pop("clazz")

        field_content_type_properties = []
        _field_content_type_properties = d.pop("fieldContentTypeProperties", UNSET)
        for field_content_type_properties_item_data in _field_content_type_properties or []:
            field_content_type_properties_item = FieldFieldContentTypePropertiesItem(
                field_content_type_properties_item_data
            )

            field_content_type_properties.append(field_content_type_properties_item)

        field = cls(
            clazz=clazz,
            field_content_type_properties=field_content_type_properties,
        )

        field.additional_properties = d
        return field

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
