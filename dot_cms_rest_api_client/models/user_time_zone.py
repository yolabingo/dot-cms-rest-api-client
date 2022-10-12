from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserTimeZone")


@attr.s(auto_attribs=True)
class UserTimeZone:
    """
    Attributes:
        display_name (Union[Unset, str]):
        id (Union[Unset, str]):
        raw_offset (Union[Unset, int]):
        dstsavings (Union[Unset, int]):
    """

    display_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    raw_offset: Union[Unset, int] = UNSET
    dstsavings: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        id = self.id
        raw_offset = self.raw_offset
        dstsavings = self.dstsavings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if raw_offset is not UNSET:
            field_dict["rawOffset"] = raw_offset
        if dstsavings is not UNSET:
            field_dict["dstsavings"] = dstsavings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        id = d.pop("id", UNSET)

        raw_offset = d.pop("rawOffset", UNSET)

        dstsavings = d.pop("dstsavings", UNSET)

        user_time_zone = cls(
            display_name=display_name,
            id=id,
            raw_offset=raw_offset,
            dstsavings=dstsavings,
        )

        user_time_zone.additional_properties = d
        return user_time_zone

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
