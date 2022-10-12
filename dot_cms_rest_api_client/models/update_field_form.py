from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.field import Field
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFieldForm")


@attr.s(auto_attribs=True)
class UpdateFieldForm:
    """
    Attributes:
        field (Union[Unset, Field]):
    """

    field: Union[Unset, Field] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _field = d.pop("field", UNSET)
        field: Union[Unset, Field]
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = Field.from_dict(_field)

        update_field_form = cls(
            field=field,
        )

        update_field_form.additional_properties = d
        return update_field_form

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
