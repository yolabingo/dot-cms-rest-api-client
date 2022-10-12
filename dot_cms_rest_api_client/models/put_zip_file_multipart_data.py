import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.form_data_content_disposition import FormDataContentDisposition
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutZipFileMultipartData")


@attr.s(auto_attribs=True)
class PutZipFileMultipartData:
    """
    Attributes:
        file (Union[Unset, FormDataContentDisposition]):
        return_ (Union[Unset, str]):
    """

    file: Union[Unset, FormDataContentDisposition] = UNSET
    return_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        return_ = self.return_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if return_ is not UNSET:
            field_dict["return"] = return_

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.file, Unset):
            file = (None, json.dumps(self.file.to_dict()).encode(), "application/json")

        return_ = self.return_ if isinstance(self.return_, Unset) else (None, str(self.return_).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if return_ is not UNSET:
            field_dict["return"] = return_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _file = d.pop("file", UNSET)
        file: Union[Unset, FormDataContentDisposition]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FormDataContentDisposition.from_dict(_file)

        return_ = d.pop("return", UNSET)

        put_zip_file_multipart_data = cls(
            file=file,
            return_=return_,
        )

        put_zip_file_multipart_data.additional_properties = d
        return put_zip_file_multipart_data

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
