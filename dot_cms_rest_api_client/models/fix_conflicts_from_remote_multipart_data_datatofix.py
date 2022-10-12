from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="FixConflictsFromRemoteMultipartDataDATATOFIX")


@attr.s(auto_attribs=True)
class FixConflictsFromRemoteMultipartDataDATATOFIX:
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fix_conflicts_from_remote_multipart_data_datatofix = cls()

        fix_conflicts_from_remote_multipart_data_datatofix.additional_properties = d
        return fix_conflicts_from_remote_multipart_data_datatofix

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
