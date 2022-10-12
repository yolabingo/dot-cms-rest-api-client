from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteUrlForm")


@attr.s(auto_attribs=True)
class RemoteUrlForm:
    """
    Attributes:
        remote_url (Union[Unset, str]):
        file_name (Union[Unset, str]):
        access_key (Union[Unset, str]):
        url_timeout_seconds (Union[Unset, int]):
        max_file_length (Union[Unset, int]):
    """

    remote_url: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    access_key: Union[Unset, str] = UNSET
    url_timeout_seconds: Union[Unset, int] = UNSET
    max_file_length: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        remote_url = self.remote_url
        file_name = self.file_name
        access_key = self.access_key
        url_timeout_seconds = self.url_timeout_seconds
        max_file_length = self.max_file_length

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if remote_url is not UNSET:
            field_dict["remoteUrl"] = remote_url
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if url_timeout_seconds is not UNSET:
            field_dict["urlTimeoutSeconds"] = url_timeout_seconds
        if max_file_length is not UNSET:
            field_dict["maxFileLength"] = max_file_length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        remote_url = d.pop("remoteUrl", UNSET)

        file_name = d.pop("fileName", UNSET)

        access_key = d.pop("accessKey", UNSET)

        url_timeout_seconds = d.pop("urlTimeoutSeconds", UNSET)

        max_file_length = d.pop("maxFileLength", UNSET)

        remote_url_form = cls(
            remote_url=remote_url,
            file_name=file_name,
            access_key=access_key,
            url_timeout_seconds=url_timeout_seconds,
            max_file_length=max_file_length,
        )

        remote_url_form.additional_properties = d
        return remote_url_form

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
