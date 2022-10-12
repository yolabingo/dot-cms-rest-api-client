from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.container_uuid import ContainerUUID
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateLayoutColumnView")


@attr.s(auto_attribs=True)
class TemplateLayoutColumnView:
    """
    Attributes:
        containers (Union[Unset, List[ContainerUUID]]):
        width (Union[Unset, int]):
        left_offset (Union[Unset, int]):
        style_class (Union[Unset, str]):
    """

    containers: Union[Unset, List[ContainerUUID]] = UNSET
    width: Union[Unset, int] = UNSET
    left_offset: Union[Unset, int] = UNSET
    style_class: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        containers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.containers, Unset):
            containers = []
            for containers_item_data in self.containers:
                containers_item = containers_item_data.to_dict()

                containers.append(containers_item)

        width = self.width
        left_offset = self.left_offset
        style_class = self.style_class

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if containers is not UNSET:
            field_dict["containers"] = containers
        if width is not UNSET:
            field_dict["width"] = width
        if left_offset is not UNSET:
            field_dict["leftOffset"] = left_offset
        if style_class is not UNSET:
            field_dict["styleClass"] = style_class

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        containers = []
        _containers = d.pop("containers", UNSET)
        for containers_item_data in _containers or []:
            containers_item = ContainerUUID.from_dict(containers_item_data)

            containers.append(containers_item)

        width = d.pop("width", UNSET)

        left_offset = d.pop("leftOffset", UNSET)

        style_class = d.pop("styleClass", UNSET)

        template_layout_column_view = cls(
            containers=containers,
            width=width,
            left_offset=left_offset,
            style_class=style_class,
        )

        template_layout_column_view.additional_properties = d
        return template_layout_column_view

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
