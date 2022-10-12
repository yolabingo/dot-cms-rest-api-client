from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.container_uuid import ContainerUUID
from ..types import UNSET, Unset

T = TypeVar("T", bound="Sidebar")


@attr.s(auto_attribs=True)
class Sidebar:
    """
    Attributes:
        containers (Union[Unset, List[ContainerUUID]]):
        location (Union[Unset, str]):
        width (Union[Unset, str]):
        width_percent (Union[Unset, int]):
        preview (Union[Unset, bool]):
    """

    containers: Union[Unset, List[ContainerUUID]] = UNSET
    location: Union[Unset, str] = UNSET
    width: Union[Unset, str] = UNSET
    width_percent: Union[Unset, int] = UNSET
    preview: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        containers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.containers, Unset):
            containers = []
            for containers_item_data in self.containers:
                containers_item = containers_item_data.to_dict()

                containers.append(containers_item)

        location = self.location
        width = self.width
        width_percent = self.width_percent
        preview = self.preview

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if containers is not UNSET:
            field_dict["containers"] = containers
        if location is not UNSET:
            field_dict["location"] = location
        if width is not UNSET:
            field_dict["width"] = width
        if width_percent is not UNSET:
            field_dict["widthPercent"] = width_percent
        if preview is not UNSET:
            field_dict["preview"] = preview

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        containers = []
        _containers = d.pop("containers", UNSET)
        for containers_item_data in _containers or []:
            containers_item = ContainerUUID.from_dict(containers_item_data)

            containers.append(containers_item)

        location = d.pop("location", UNSET)

        width = d.pop("width", UNSET)

        width_percent = d.pop("widthPercent", UNSET)

        preview = d.pop("preview", UNSET)

        sidebar = cls(
            containers=containers,
            location=location,
            width=width,
            width_percent=width_percent,
            preview=preview,
        )

        sidebar.additional_properties = d
        return sidebar

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
