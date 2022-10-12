from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.template_layout_column import TemplateLayoutColumn
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateLayoutRow")


@attr.s(auto_attribs=True)
class TemplateLayoutRow:
    """
    Attributes:
        columns (Union[Unset, List[TemplateLayoutColumn]]):
        style_class (Union[Unset, str]):
    """

    columns: Union[Unset, List[TemplateLayoutColumn]] = UNSET
    style_class: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()

                columns.append(columns_item)

        style_class = self.style_class

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if style_class is not UNSET:
            field_dict["styleClass"] = style_class

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = TemplateLayoutColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        style_class = d.pop("styleClass", UNSET)

        template_layout_row = cls(
            columns=columns,
            style_class=style_class,
        )

        template_layout_row.additional_properties = d
        return template_layout_row

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
