import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.form_data_content_disposition_parameters import FormDataContentDispositionParameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="FormDataContentDisposition")


@attr.s(auto_attribs=True)
class FormDataContentDisposition:
    """
    Attributes:
        type (Union[Unset, str]):
        parameters (Union[Unset, FormDataContentDispositionParameters]):
        file_name (Union[Unset, str]):
        creation_date (Union[Unset, datetime.datetime]):
        modification_date (Union[Unset, datetime.datetime]):
        read_date (Union[Unset, datetime.datetime]):
        size (Union[Unset, int]):
        name (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    parameters: Union[Unset, FormDataContentDispositionParameters] = UNSET
    file_name: Union[Unset, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    modification_date: Union[Unset, datetime.datetime] = UNSET
    read_date: Union[Unset, datetime.datetime] = UNSET
    size: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        file_name = self.file_name
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        modification_date: Union[Unset, str] = UNSET
        if not isinstance(self.modification_date, Unset):
            modification_date = self.modification_date.isoformat()

        read_date: Union[Unset, str] = UNSET
        if not isinstance(self.read_date, Unset):
            read_date = self.read_date.isoformat()

        size = self.size
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if modification_date is not UNSET:
            field_dict["modificationDate"] = modification_date
        if read_date is not UNSET:
            field_dict["readDate"] = read_date
        if size is not UNSET:
            field_dict["size"] = size
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, FormDataContentDispositionParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = FormDataContentDispositionParameters.from_dict(_parameters)

        file_name = d.pop("fileName", UNSET)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _modification_date = d.pop("modificationDate", UNSET)
        modification_date: Union[Unset, datetime.datetime]
        if isinstance(_modification_date, Unset):
            modification_date = UNSET
        else:
            modification_date = isoparse(_modification_date)

        _read_date = d.pop("readDate", UNSET)
        read_date: Union[Unset, datetime.datetime]
        if isinstance(_read_date, Unset):
            read_date = UNSET
        else:
            read_date = isoparse(_read_date)

        size = d.pop("size", UNSET)

        name = d.pop("name", UNSET)

        form_data_content_disposition = cls(
            type=type,
            parameters=parameters,
            file_name=file_name,
            creation_date=creation_date,
            modification_date=modification_date,
            read_date=read_date,
            size=size,
            name=name,
        )

        form_data_content_disposition.additional_properties = d
        return form_data_content_disposition

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
