from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tuple_2_system_action_string_1 import Tuple2SystemActionString1
from ..types import UNSET, Unset

T = TypeVar("T", bound="Tuple2SystemActionString")


@attr.s(auto_attribs=True)
class Tuple2SystemActionString:
    """
    Attributes:
        field_1 (Union[Unset, Tuple2SystemActionString1]):
        field_2 (Union[Unset, str]):
    """

    field_1: Union[Unset, Tuple2SystemActionString1] = UNSET
    field_2: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_1: Union[Unset, str] = UNSET
        if not isinstance(self.field_1, Unset):
            field_1 = self.field_1.value

        field_2 = self.field_2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_1 is not UNSET:
            field_dict["_1"] = field_1
        if field_2 is not UNSET:
            field_dict["_2"] = field_2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _field_1 = d.pop("_1", UNSET)
        field_1: Union[Unset, Tuple2SystemActionString1]
        if isinstance(_field_1, Unset):
            field_1 = UNSET
        else:
            field_1 = Tuple2SystemActionString1(_field_1)

        field_2 = d.pop("_2", UNSET)

        tuple_2_system_action_string = cls(
            field_1=field_1,
            field_2=field_2,
        )

        tuple_2_system_action_string.additional_properties = d
        return tuple_2_system_action_string

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
