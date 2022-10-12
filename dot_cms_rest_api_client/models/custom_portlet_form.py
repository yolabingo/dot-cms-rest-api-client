from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomPortletForm")


@attr.s(auto_attribs=True)
class CustomPortletForm:
    """
    Attributes:
        portlet_id (Union[Unset, str]):
        portlet_name (Union[Unset, str]):
        base_types (Union[Unset, str]):
        content_types (Union[Unset, str]):
        data_view_mode (Union[Unset, str]):
    """

    portlet_id: Union[Unset, str] = UNSET
    portlet_name: Union[Unset, str] = UNSET
    base_types: Union[Unset, str] = UNSET
    content_types: Union[Unset, str] = UNSET
    data_view_mode: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        portlet_id = self.portlet_id
        portlet_name = self.portlet_name
        base_types = self.base_types
        content_types = self.content_types
        data_view_mode = self.data_view_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portlet_id is not UNSET:
            field_dict["portletId"] = portlet_id
        if portlet_name is not UNSET:
            field_dict["portletName"] = portlet_name
        if base_types is not UNSET:
            field_dict["baseTypes"] = base_types
        if content_types is not UNSET:
            field_dict["contentTypes"] = content_types
        if data_view_mode is not UNSET:
            field_dict["dataViewMode"] = data_view_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        portlet_id = d.pop("portletId", UNSET)

        portlet_name = d.pop("portletName", UNSET)

        base_types = d.pop("baseTypes", UNSET)

        content_types = d.pop("contentTypes", UNSET)

        data_view_mode = d.pop("dataViewMode", UNSET)

        custom_portlet_form = cls(
            portlet_id=portlet_id,
            portlet_name=portlet_name,
            base_types=base_types,
            content_types=content_types,
            data_view_mode=data_view_mode,
        )

        custom_portlet_form.additional_properties = d
        return custom_portlet_form

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
