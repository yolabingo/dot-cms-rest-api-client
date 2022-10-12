from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchForm")


@attr.s(auto_attribs=True)
class SearchForm:
    """
    Attributes:
        query (Union[Unset, str]):
        sort (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        user_id (Union[Unset, str]):
        render (Union[Unset, str]):
        depth (Union[Unset, int]):
        language_id (Union[Unset, int]):
        all_categories_info (Union[Unset, bool]):
    """

    query: Union[Unset, str] = UNSET
    sort: Union[Unset, str] = UNSET
    limit: Union[Unset, int] = UNSET
    offset: Union[Unset, int] = UNSET
    user_id: Union[Unset, str] = UNSET
    render: Union[Unset, str] = UNSET
    depth: Union[Unset, int] = UNSET
    language_id: Union[Unset, int] = UNSET
    all_categories_info: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query
        sort = self.sort
        limit = self.limit
        offset = self.offset
        user_id = self.user_id
        render = self.render
        depth = self.depth
        language_id = self.language_id
        all_categories_info = self.all_categories_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if sort is not UNSET:
            field_dict["sort"] = sort
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if render is not UNSET:
            field_dict["render"] = render
        if depth is not UNSET:
            field_dict["depth"] = depth
        if language_id is not UNSET:
            field_dict["languageId"] = language_id
        if all_categories_info is not UNSET:
            field_dict["allCategoriesInfo"] = all_categories_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query = d.pop("query", UNSET)

        sort = d.pop("sort", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        user_id = d.pop("userId", UNSET)

        render = d.pop("render", UNSET)

        depth = d.pop("depth", UNSET)

        language_id = d.pop("languageId", UNSET)

        all_categories_info = d.pop("allCategoriesInfo", UNSET)

        search_form = cls(
            query=query,
            sort=sort,
            limit=limit,
            offset=offset,
            user_id=user_id,
            render=render,
            depth=depth,
            language_id=language_id,
            all_categories_info=all_categories_info,
        )

        search_form.additional_properties = d
        return search_form

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
