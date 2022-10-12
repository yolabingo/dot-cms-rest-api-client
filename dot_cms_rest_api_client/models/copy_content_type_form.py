from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CopyContentTypeForm")


@attr.s(auto_attribs=True)
class CopyContentTypeForm:
    """
    Attributes:
        name (str):
        variable (Union[Unset, str]):
        folder (Union[Unset, str]):
        host (Union[Unset, str]):
        icon (Union[Unset, str]):
    """

    name: str
    variable: Union[Unset, str] = UNSET
    folder: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        variable = self.variable
        folder = self.folder
        host = self.host
        icon = self.icon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if variable is not UNSET:
            field_dict["variable"] = variable
        if folder is not UNSET:
            field_dict["folder"] = folder
        if host is not UNSET:
            field_dict["host"] = host
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        variable = d.pop("variable", UNSET)

        folder = d.pop("folder", UNSET)

        host = d.pop("host", UNSET)

        icon = d.pop("icon", UNSET)

        copy_content_type_form = cls(
            name=name,
            variable=variable,
            folder=folder,
            host=host,
            icon=icon,
        )

        copy_content_type_form.additional_properties = d
        return copy_content_type_form

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
