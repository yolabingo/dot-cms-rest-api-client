from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.container_entry import ContainerEntry
from ..types import UNSET, Unset

T = TypeVar("T", bound="PageContainerForm")


@attr.s(auto_attribs=True)
class PageContainerForm:
    """
    Attributes:
        request_json (Union[Unset, str]):
        container_entries (Union[Unset, List[ContainerEntry]]):
    """

    request_json: Union[Unset, str] = UNSET
    container_entries: Union[Unset, List[ContainerEntry]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_json = self.request_json
        container_entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.container_entries, Unset):
            container_entries = []
            for container_entries_item_data in self.container_entries:
                container_entries_item = container_entries_item_data.to_dict()

                container_entries.append(container_entries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_json is not UNSET:
            field_dict["requestJson"] = request_json
        if container_entries is not UNSET:
            field_dict["containerEntries"] = container_entries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_json = d.pop("requestJson", UNSET)

        container_entries = []
        _container_entries = d.pop("containerEntries", UNSET)
        for container_entries_item_data in _container_entries or []:
            container_entries_item = ContainerEntry.from_dict(container_entries_item_data)

            container_entries.append(container_entries_item)

        page_container_form = cls(
            request_json=request_json,
            container_entries=container_entries,
        )

        page_container_form.additional_properties = d
        return page_container_form

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
