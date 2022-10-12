from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkActionForm")


@attr.s(auto_attribs=True)
class BulkActionForm:
    """
    Attributes:
        contentlet_ids (Union[Unset, List[str]]):
        query (Union[Unset, str]):
    """

    contentlet_ids: Union[Unset, List[str]] = UNSET
    query: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contentlet_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contentlet_ids, Unset):
            contentlet_ids = self.contentlet_ids

        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contentlet_ids is not UNSET:
            field_dict["contentletIds"] = contentlet_ids
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contentlet_ids = cast(List[str], d.pop("contentletIds", UNSET))

        query = d.pop("query", UNSET)

        bulk_action_form = cls(
            contentlet_ids=contentlet_ids,
            query=query,
        )

        bulk_action_form.additional_properties = d
        return bulk_action_form

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
