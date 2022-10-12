from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.template_layout_row_view import TemplateLayoutRowView
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyView")


@attr.s(auto_attribs=True)
class BodyView:
    """
    Attributes:
        rows (Union[Unset, List[TemplateLayoutRowView]]):
    """

    rows: Union[Unset, List[TemplateLayoutRowView]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()

                rows.append(rows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = TemplateLayoutRowView.from_dict(rows_item_data)

            rows.append(rows_item)

        body_view = cls(
            rows=rows,
        )

        body_view.additional_properties = d
        return body_view

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
