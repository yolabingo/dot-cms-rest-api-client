from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTag")


@attr.s(auto_attribs=True)
class RestTag:
    """
    Attributes:
        label (Union[Unset, str]):
        site_id (Union[Unset, str]):
        site_name (Union[Unset, str]):
        persona (Union[Unset, bool]):
        id (Union[Unset, str]):
    """

    label: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    persona: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        site_id = self.site_id
        site_name = self.site_name
        persona = self.persona
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if persona is not UNSET:
            field_dict["persona"] = persona
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label", UNSET)

        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        persona = d.pop("persona", UNSET)

        id = d.pop("id", UNSET)

        rest_tag = cls(
            label=label,
            site_id=site_id,
            site_name=site_name,
            persona=persona,
            id=id,
        )

        rest_tag.additional_properties = d
        return rest_tag

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
