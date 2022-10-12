from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.template_layout import TemplateLayout
from ..types import UNSET, Unset

T = TypeVar("T", bound="PageForm")


@attr.s(auto_attribs=True)
class PageForm:
    """
    Attributes:
        theme_id (Union[Unset, str]):
        title (Union[Unset, str]):
        host_id (Union[Unset, str]):
        layout (Union[Unset, TemplateLayout]):
        anonymous_layout (Union[Unset, bool]):
    """

    theme_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    host_id: Union[Unset, str] = UNSET
    layout: Union[Unset, TemplateLayout] = UNSET
    anonymous_layout: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        theme_id = self.theme_id
        title = self.title
        host_id = self.host_id
        layout: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.layout, Unset):
            layout = self.layout.to_dict()

        anonymous_layout = self.anonymous_layout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if theme_id is not UNSET:
            field_dict["themeId"] = theme_id
        if title is not UNSET:
            field_dict["title"] = title
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if layout is not UNSET:
            field_dict["layout"] = layout
        if anonymous_layout is not UNSET:
            field_dict["anonymousLayout"] = anonymous_layout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        theme_id = d.pop("themeId", UNSET)

        title = d.pop("title", UNSET)

        host_id = d.pop("hostId", UNSET)

        _layout = d.pop("layout", UNSET)
        layout: Union[Unset, TemplateLayout]
        if isinstance(_layout, Unset):
            layout = UNSET
        else:
            layout = TemplateLayout.from_dict(_layout)

        anonymous_layout = d.pop("anonymousLayout", UNSET)

        page_form = cls(
            theme_id=theme_id,
            title=title,
            host_id=host_id,
            layout=layout,
            anonymous_layout=anonymous_layout,
        )

        page_form.additional_properties = d
        return page_form

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
