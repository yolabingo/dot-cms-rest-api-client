from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rest_condition_group_conditions import RestConditionGroupConditions
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestConditionGroup")


@attr.s(auto_attribs=True)
class RestConditionGroup:
    """
    Attributes:
        operator (str):
        priority (Union[Unset, int]):
        conditions (Union[Unset, RestConditionGroupConditions]):
    """

    operator: str
    priority: Union[Unset, int] = UNSET
    conditions: Union[Unset, RestConditionGroupConditions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operator = self.operator
        priority = self.priority
        conditions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operator = d.pop("operator")

        priority = d.pop("priority", UNSET)

        _conditions = d.pop("conditions", UNSET)
        conditions: Union[Unset, RestConditionGroupConditions]
        if isinstance(_conditions, Unset):
            conditions = UNSET
        else:
            conditions = RestConditionGroupConditions.from_dict(_conditions)

        rest_condition_group = cls(
            operator=operator,
            priority=priority,
            conditions=conditions,
        )

        rest_condition_group.additional_properties = d
        return rest_condition_group

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
