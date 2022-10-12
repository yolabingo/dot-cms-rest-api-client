from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.remote_api_token_form_token_info import RemoteAPITokenFormTokenInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteAPITokenForm")


@attr.s(auto_attribs=True)
class RemoteAPITokenForm:
    """
    Attributes:
        token_info (Union[Unset, RemoteAPITokenFormTokenInfo]):
    """

    token_info: Union[Unset, RemoteAPITokenFormTokenInfo] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.token_info, Unset):
            token_info = self.token_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token_info is not UNSET:
            field_dict["tokenInfo"] = token_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _token_info = d.pop("tokenInfo", UNSET)
        token_info: Union[Unset, RemoteAPITokenFormTokenInfo]
        if isinstance(_token_info, Unset):
            token_info = UNSET
        else:
            token_info = RemoteAPITokenFormTokenInfo.from_dict(_token_info)

        remote_api_token_form = cls(
            token_info=token_info,
        )

        remote_api_token_form.additional_properties = d
        return remote_api_token_form

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
