from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.container_uuid import ContainerUUID
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateLayoutColumn")


@attr.s(auto_attribs=True)
class TemplateLayoutColumn:
    """
    Attributes:
        containers (Union[Unset, List[ContainerUUID]]):
        width_percent (Union[Unset, int]):
        left_offset (Union[Unset, int]):
        style_class (Union[Unset, str]):
        preview (Union[Unset, bool]):
        width (Union[Unset, int]):
        left (Union[Unset, int]):
    """

    containers: Union[Unset, List[ContainerUUID]] = UNSET
    width_percent: Union[Unset, int] = UNSET
    left_offset: Union[Unset, int] = UNSET
    style_class: Union[Unset, str] = UNSET
    preview: Union[Unset, bool] = UNSET
    width: Union[Unset, int] = UNSET
    left: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        containers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.containers, Unset):
            containers = []
            for containers_item_data in self.containers:
                containers_item = containers_item_data.to_dict()

                containers.append(containers_item)

        width_percent = self.width_percent
        left_offset = self.left_offset
        style_class = self.style_class
        preview = self.preview
        width = self.width
        left = self.left

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if containers is not UNSET:
            field_dict["containers"] = containers
        if width_percent is not UNSET:
            field_dict["widthPercent"] = width_percent
        if left_offset is not UNSET:
            field_dict["leftOffset"] = left_offset
        if style_class is not UNSET:
            field_dict["styleClass"] = style_class
        if preview is not UNSET:
            field_dict["preview"] = preview
        if width is not UNSET:
            field_dict["width"] = width
        if left is not UNSET:
            field_dict["left"] = left

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        containers = []
        _containers = d.pop("containers", UNSET)
        for containers_item_data in _containers or []:
            containers_item = ContainerUUID.from_dict(containers_item_data)

            containers.append(containers_item)

        width_percent = d.pop("widthPercent", UNSET)

        left_offset = d.pop("leftOffset", UNSET)

        style_class = d.pop("styleClass", UNSET)

        preview = d.pop("preview", UNSET)

        width = d.pop("width", UNSET)

        left = d.pop("left", UNSET)

        template_layout_column = cls(
            containers=containers,
            width_percent=width_percent,
            left_offset=left_offset,
            style_class=style_class,
            preview=preview,
            width=width,
            left=left,
        )

        template_layout_column.additional_properties = d
        return template_layout_column

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
