from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.event_output_type import EventOutputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventOutput")


@attr.s(auto_attribs=True)
class EventOutput:
    """
    Attributes:
        type (Union[Unset, EventOutputType]):
        closed (Union[Unset, bool]):
    """

    type: Union[Unset, EventOutputType] = UNSET
    closed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        closed = self.closed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if closed is not UNSET:
            field_dict["closed"] = closed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, EventOutputType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EventOutputType.from_dict(_type)

        closed = d.pop("closed", UNSET)

        event_output = cls(
            type=type,
            closed=closed,
        )

        event_output.additional_properties = d
        return event_output

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
