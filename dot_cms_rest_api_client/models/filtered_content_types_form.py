from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.filtered_content_types_form_filter import FilteredContentTypesFormFilter
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilteredContentTypesForm")


@attr.s(auto_attribs=True)
class FilteredContentTypesForm:
    """
    Attributes:
        filter_ (Union[Unset, FilteredContentTypesFormFilter]):
        page (Union[Unset, int]):
        per_page (Union[Unset, int]):
        order_by (Union[Unset, str]):
        direction (Union[Unset, str]):
    """

    filter_: Union[Unset, FilteredContentTypesFormFilter] = UNSET
    page: Union[Unset, int] = UNSET
    per_page: Union[Unset, int] = UNSET
    order_by: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        page = self.page
        per_page = self.per_page
        order_by = self.order_by
        direction = self.direction

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if page is not UNSET:
            field_dict["page"] = page
        if per_page is not UNSET:
            field_dict["perPage"] = per_page
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, FilteredContentTypesFormFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = FilteredContentTypesFormFilter.from_dict(_filter_)

        page = d.pop("page", UNSET)

        per_page = d.pop("perPage", UNSET)

        order_by = d.pop("orderBy", UNSET)

        direction = d.pop("direction", UNSET)

        filtered_content_types_form = cls(
            filter_=filter_,
            page=page,
            per_page=per_page,
            order_by=order_by,
            direction=direction,
        )

        filtered_content_types_form.additional_properties = d
        return filtered_content_types_form

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
