from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.body_view import BodyView
from ..models.sidebar_view import SidebarView
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateLayoutView")


@attr.s(auto_attribs=True)
class TemplateLayoutView:
    """
    Attributes:
        width (Union[Unset, str]):
        title (Union[Unset, str]):
        header (Union[Unset, bool]):
        footer (Union[Unset, bool]):
        body (Union[Unset, BodyView]):
        sidebar (Union[Unset, SidebarView]):
    """

    width: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    header: Union[Unset, bool] = UNSET
    footer: Union[Unset, bool] = UNSET
    body: Union[Unset, BodyView] = UNSET
    sidebar: Union[Unset, SidebarView] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        width = self.width
        title = self.title
        header = self.header
        footer = self.footer
        body: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        sidebar: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sidebar, Unset):
            sidebar = self.sidebar.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if title is not UNSET:
            field_dict["title"] = title
        if header is not UNSET:
            field_dict["header"] = header
        if footer is not UNSET:
            field_dict["footer"] = footer
        if body is not UNSET:
            field_dict["body"] = body
        if sidebar is not UNSET:
            field_dict["sidebar"] = sidebar

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        width = d.pop("width", UNSET)

        title = d.pop("title", UNSET)

        header = d.pop("header", UNSET)

        footer = d.pop("footer", UNSET)

        _body = d.pop("body", UNSET)
        body: Union[Unset, BodyView]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = BodyView.from_dict(_body)

        _sidebar = d.pop("sidebar", UNSET)
        sidebar: Union[Unset, SidebarView]
        if isinstance(_sidebar, Unset):
            sidebar = UNSET
        else:
            sidebar = SidebarView.from_dict(_sidebar)

        template_layout_view = cls(
            width=width,
            title=title,
            header=header,
            footer=footer,
            body=body,
            sidebar=sidebar,
        )

        template_layout_view.additional_properties = d
        return template_layout_view

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
