from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UpdateTagForm")


@attr.s(auto_attribs=True)
class UpdateTagForm:
    """
    Attributes:
        site_id (str):
        tag_name (str):
        tag_id (str):
    """

    site_id: str
    tag_name: str
    tag_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        site_id = self.site_id
        tag_name = self.tag_name
        tag_id = self.tag_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteId": site_id,
                "tagName": tag_name,
                "tagId": tag_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        site_id = d.pop("siteId")

        tag_name = d.pop("tagName")

        tag_id = d.pop("tagId")

        update_tag_form = cls(
            site_id=site_id,
            tag_name=tag_name,
            tag_id=tag_id,
        )

        update_tag_form.additional_properties = d
        return update_tag_form

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
