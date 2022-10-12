from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rest_rule_action_parameters import RestRuleActionParameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRuleAction")


@attr.s(auto_attribs=True)
class RestRuleAction:
    """
    Attributes:
        owning_rule (str):
        actionlet (str):
        priority (Union[Unset, int]):
        parameters (Union[Unset, RestRuleActionParameters]):
    """

    owning_rule: str
    actionlet: str
    priority: Union[Unset, int] = UNSET
    parameters: Union[Unset, RestRuleActionParameters] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owning_rule = self.owning_rule
        actionlet = self.actionlet
        priority = self.priority
        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owningRule": owning_rule,
                "actionlet": actionlet,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owning_rule = d.pop("owningRule")

        actionlet = d.pop("actionlet")

        priority = d.pop("priority", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, RestRuleActionParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = RestRuleActionParameters.from_dict(_parameters)

        rest_rule_action = cls(
            owning_rule=owning_rule,
            actionlet=actionlet,
            priority=priority,
            parameters=parameters,
        )

        rest_rule_action.additional_properties = d
        return rest_rule_action

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
