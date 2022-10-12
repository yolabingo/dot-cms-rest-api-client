from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteFieldsForm")


@attr.s(auto_attribs=True)
class DeleteFieldsForm:
    """
    Attributes:
        fields_id (Union[Unset, List[str]]):
    """

    fields_id: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fields_id: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fields_id, Unset):
            fields_id = self.fields_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields_id is not UNSET:
            field_dict["fieldsID"] = fields_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fields_id = cast(List[str], d.pop("fieldsID", UNSET))

        delete_fields_form = cls(
            fields_id=fields_id,
        )

        delete_fields_form.additional_properties = d
        return delete_fields_form

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
