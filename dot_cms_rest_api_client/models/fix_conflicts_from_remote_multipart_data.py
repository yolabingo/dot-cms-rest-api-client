import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.fix_conflicts_from_remote_multipart_data_datatofix import FixConflictsFromRemoteMultipartDataDATATOFIX
from ..types import UNSET, Unset

T = TypeVar("T", bound="FixConflictsFromRemoteMultipartData")


@attr.s(auto_attribs=True)
class FixConflictsFromRemoteMultipartData:
    """
    Attributes:
        data_to_fix (Union[Unset, FixConflictsFromRemoteMultipartDataDATATOFIX]):
        type (Union[Unset, str]):
    """

    data_to_fix: Union[Unset, FixConflictsFromRemoteMultipartDataDATATOFIX] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_to_fix: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_to_fix, Unset):
            data_to_fix = self.data_to_fix.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_to_fix is not UNSET:
            field_dict["DATA_TO_FIX"] = data_to_fix
        if type is not UNSET:
            field_dict["TYPE"] = type

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        data_to_fix: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.data_to_fix, Unset):
            data_to_fix = (None, json.dumps(self.data_to_fix.to_dict()).encode(), "application/json")

        type = self.type if isinstance(self.type, Unset) else (None, str(self.type).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if data_to_fix is not UNSET:
            field_dict["DATA_TO_FIX"] = data_to_fix
        if type is not UNSET:
            field_dict["TYPE"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _data_to_fix = d.pop("DATA_TO_FIX", UNSET)
        data_to_fix: Union[Unset, FixConflictsFromRemoteMultipartDataDATATOFIX]
        if isinstance(_data_to_fix, Unset):
            data_to_fix = UNSET
        else:
            data_to_fix = FixConflictsFromRemoteMultipartDataDATATOFIX.from_dict(_data_to_fix)

        type = d.pop("TYPE", UNSET)

        fix_conflicts_from_remote_multipart_data = cls(
            data_to_fix=data_to_fix,
            type=type,
        )

        fix_conflicts_from_remote_multipart_data.additional_properties = d
        return fix_conflicts_from_remote_multipart_data

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
