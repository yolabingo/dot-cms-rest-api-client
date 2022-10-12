from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rest_rule_condition_groups import RestRuleConditionGroups
from ..models.rest_rule_rule_actions import RestRuleRuleActions
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRule")


@attr.s(auto_attribs=True)
class RestRule:
    """
    Attributes:
        name (str):
        fire_on (Union[Unset, str]):
        short_circuit (Union[Unset, bool]):
        priority (Union[Unset, int]):
        enabled (Union[Unset, bool]):
        condition_groups (Union[Unset, RestRuleConditionGroups]):
        rule_actions (Union[Unset, RestRuleRuleActions]):
    """

    name: str
    fire_on: Union[Unset, str] = UNSET
    short_circuit: Union[Unset, bool] = UNSET
    priority: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    condition_groups: Union[Unset, RestRuleConditionGroups] = UNSET
    rule_actions: Union[Unset, RestRuleRuleActions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        fire_on = self.fire_on
        short_circuit = self.short_circuit
        priority = self.priority
        enabled = self.enabled
        condition_groups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.condition_groups, Unset):
            condition_groups = self.condition_groups.to_dict()

        rule_actions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rule_actions, Unset):
            rule_actions = self.rule_actions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if fire_on is not UNSET:
            field_dict["fireOn"] = fire_on
        if short_circuit is not UNSET:
            field_dict["shortCircuit"] = short_circuit
        if priority is not UNSET:
            field_dict["priority"] = priority
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if condition_groups is not UNSET:
            field_dict["conditionGroups"] = condition_groups
        if rule_actions is not UNSET:
            field_dict["ruleActions"] = rule_actions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        fire_on = d.pop("fireOn", UNSET)

        short_circuit = d.pop("shortCircuit", UNSET)

        priority = d.pop("priority", UNSET)

        enabled = d.pop("enabled", UNSET)

        _condition_groups = d.pop("conditionGroups", UNSET)
        condition_groups: Union[Unset, RestRuleConditionGroups]
        if isinstance(_condition_groups, Unset):
            condition_groups = UNSET
        else:
            condition_groups = RestRuleConditionGroups.from_dict(_condition_groups)

        _rule_actions = d.pop("ruleActions", UNSET)
        rule_actions: Union[Unset, RestRuleRuleActions]
        if isinstance(_rule_actions, Unset):
            rule_actions = UNSET
        else:
            rule_actions = RestRuleRuleActions.from_dict(_rule_actions)

        rest_rule = cls(
            name=name,
            fire_on=fire_on,
            short_circuit=short_circuit,
            priority=priority,
            enabled=enabled,
            condition_groups=condition_groups,
            rule_actions=rule_actions,
        )

        rest_rule.additional_properties = d
        return rest_rule

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
