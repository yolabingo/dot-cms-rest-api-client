from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerEntry")


@attr.s(auto_attribs=True)
class ContainerEntry:
    """
    Attributes:
        persona_tag (Union[Unset, str]):
        content_ids (Union[Unset, List[str]]):
        container_id (Union[Unset, str]):
        container_uuid (Union[Unset, str]):
    """

    persona_tag: Union[Unset, str] = UNSET
    content_ids: Union[Unset, List[str]] = UNSET
    container_id: Union[Unset, str] = UNSET
    container_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        persona_tag = self.persona_tag
        content_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.content_ids, Unset):
            content_ids = self.content_ids

        container_id = self.container_id
        container_uuid = self.container_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if persona_tag is not UNSET:
            field_dict["personaTag"] = persona_tag
        if content_ids is not UNSET:
            field_dict["contentIds"] = content_ids
        if container_id is not UNSET:
            field_dict["containerId"] = container_id
        if container_uuid is not UNSET:
            field_dict["containerUUID"] = container_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        persona_tag = d.pop("personaTag", UNSET)

        content_ids = cast(List[str], d.pop("contentIds", UNSET))

        container_id = d.pop("containerId", UNSET)

        container_uuid = d.pop("containerUUID", UNSET)

        container_entry = cls(
            persona_tag=persona_tag,
            content_ids=content_ids,
            container_id=container_id,
            container_uuid=container_uuid,
        )

        container_entry.additional_properties = d
        return container_entry

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
