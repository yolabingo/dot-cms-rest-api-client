from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.filter_descriptor_form_filters import FilterDescriptorFormFilters
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterDescriptorForm")


@attr.s(auto_attribs=True)
class FilterDescriptorForm:
    """
    Attributes:
        key (Union[Unset, str]):
        title (Union[Unset, str]):
        sort (Union[Unset, str]):
        default_filter (Union[Unset, bool]):
        roles (Union[Unset, str]):
        filters (Union[Unset, FilterDescriptorFormFilters]):
    """

    key: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    sort: Union[Unset, str] = UNSET
    default_filter: Union[Unset, bool] = UNSET
    roles: Union[Unset, str] = UNSET
    filters: Union[Unset, FilterDescriptorFormFilters] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        title = self.title
        sort = self.sort
        default_filter = self.default_filter
        roles = self.roles
        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if title is not UNSET:
            field_dict["title"] = title
        if sort is not UNSET:
            field_dict["sort"] = sort
        if default_filter is not UNSET:
            field_dict["defaultFilter"] = default_filter
        if roles is not UNSET:
            field_dict["roles"] = roles
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        title = d.pop("title", UNSET)

        sort = d.pop("sort", UNSET)

        default_filter = d.pop("defaultFilter", UNSET)

        roles = d.pop("roles", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, FilterDescriptorFormFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = FilterDescriptorFormFilters.from_dict(_filters)

        filter_descriptor_form = cls(
            key=key,
            title=title,
            sort=sort,
            default_filter=default_filter,
            roles=roles,
            filters=filters,
        )

        filter_descriptor_form.additional_properties = d
        return filter_descriptor_form

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
