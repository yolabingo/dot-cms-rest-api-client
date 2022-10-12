from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tag_form_tags import TagFormTags
from ..types import UNSET, Unset

T = TypeVar("T", bound="TagForm")


@attr.s(auto_attribs=True)
class TagForm:
    """
    Attributes:
        tags (TagFormTags):
        owner_id (Union[Unset, str]):
    """

    tags: TagFormTags
    owner_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tags = self.tags.to_dict()

        owner_id = self.owner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags": tags,
            }
        )
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tags = TagFormTags.from_dict(d.pop("tags"))

        owner_id = d.pop("ownerId", UNSET)

        tag_form = cls(
            tags=tags,
            owner_id=owner_id,
        )

        tag_form.additional_properties = d
        return tag_form

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
