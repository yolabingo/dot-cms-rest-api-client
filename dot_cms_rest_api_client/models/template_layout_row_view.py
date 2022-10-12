from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.template_layout_column_view import TemplateLayoutColumnView
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateLayoutRowView")


@attr.s(auto_attribs=True)
class TemplateLayoutRowView:
    """
    Attributes:
        style_class (Union[Unset, str]):
        columns (Union[Unset, List[TemplateLayoutColumnView]]):
    """

    style_class: Union[Unset, str] = UNSET
    columns: Union[Unset, List[TemplateLayoutColumnView]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        style_class = self.style_class
        columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()

                columns.append(columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if style_class is not UNSET:
            field_dict["styleClass"] = style_class
        if columns is not UNSET:
            field_dict["columns"] = columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        style_class = d.pop("styleClass", UNSET)

        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = TemplateLayoutColumnView.from_dict(columns_item_data)

            columns.append(columns_item)

        template_layout_row_view = cls(
            style_class=style_class,
            columns=columns,
        )

        template_layout_row_view.additional_properties = d
        return template_layout_row_view

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
