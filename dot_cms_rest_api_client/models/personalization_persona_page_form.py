from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PersonalizationPersonaPageForm")


@attr.s(auto_attribs=True)
class PersonalizationPersonaPageForm:
    """
    Attributes:
        page_id (str):
        persona_tag (str):
    """

    page_id: str
    persona_tag: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_id = self.page_id
        persona_tag = self.persona_tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pageId": page_id,
                "personaTag": persona_tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_id = d.pop("pageId")

        persona_tag = d.pop("personaTag")

        personalization_persona_page_form = cls(
            page_id=page_id,
            persona_tag=persona_tag,
        )

        personalization_persona_page_form.additional_properties = d
        return personalization_persona_page_form

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
