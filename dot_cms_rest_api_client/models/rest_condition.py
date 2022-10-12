from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rest_condition_values import RestConditionValues
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestCondition")


@attr.s(auto_attribs=True)
class RestCondition:
    """
    Attributes:
        owning_group (str):
        conditionlet (str):
        operator (str):
        values (Union[Unset, RestConditionValues]):
        priority (Union[Unset, int]):
    """

    owning_group: str
    conditionlet: str
    operator: str
    values: Union[Unset, RestConditionValues] = UNSET
    priority: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owning_group = self.owning_group
        conditionlet = self.conditionlet
        operator = self.operator
        values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        priority = self.priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owningGroup": owning_group,
                "conditionlet": conditionlet,
                "operator": operator,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owning_group = d.pop("owningGroup")

        conditionlet = d.pop("conditionlet")

        operator = d.pop("operator")

        _values = d.pop("values", UNSET)
        values: Union[Unset, RestConditionValues]
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = RestConditionValues.from_dict(_values)

        priority = d.pop("priority", UNSET)

        rest_condition = cls(
            owning_group=owning_group,
            conditionlet=conditionlet,
            operator=operator,
            values=values,
            priority=priority,
        )

        rest_condition.additional_properties = d
        return rest_condition

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
