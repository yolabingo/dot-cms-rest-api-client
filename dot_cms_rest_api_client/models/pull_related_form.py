from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullRelatedForm")


@attr.s(auto_attribs=True)
class PullRelatedForm:
    """
    Attributes:
        field_variable (str):
        identifier (str):
        limit (int):
        offset (int):
        order_by (str):
        condition (Union[Unset, str]):
    """

    field_variable: str
    identifier: str
    limit: int
    offset: int
    order_by: str
    condition: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_variable = self.field_variable
        identifier = self.identifier
        limit = self.limit
        offset = self.offset
        order_by = self.order_by
        condition = self.condition

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldVariable": field_variable,
                "identifier": identifier,
                "limit": limit,
                "offset": offset,
                "orderBy": order_by,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_variable = d.pop("fieldVariable")

        identifier = d.pop("identifier")

        limit = d.pop("limit")

        offset = d.pop("offset")

        order_by = d.pop("orderBy")

        condition = d.pop("condition", UNSET)

        pull_related_form = cls(
            field_variable=field_variable,
            identifier=identifier,
            limit=limit,
            offset=offset,
            order_by=order_by,
            condition=condition,
        )

        pull_related_form.additional_properties = d
        return pull_related_form

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
