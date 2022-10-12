from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowStepUpdateForm")


@attr.s(auto_attribs=True)
class WorkflowStepUpdateForm:
    """
    Attributes:
        step_order (int):
        step_name (str):
        enable_escalation (bool):
        escalation_time (str):
        step_resolved (bool):
        escalation_action (Union[Unset, str]):
    """

    step_order: int
    step_name: str
    enable_escalation: bool
    escalation_time: str
    step_resolved: bool
    escalation_action: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        step_order = self.step_order
        step_name = self.step_name
        enable_escalation = self.enable_escalation
        escalation_time = self.escalation_time
        step_resolved = self.step_resolved
        escalation_action = self.escalation_action

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stepOrder": step_order,
                "stepName": step_name,
                "enableEscalation": enable_escalation,
                "escalationTime": escalation_time,
                "stepResolved": step_resolved,
            }
        )
        if escalation_action is not UNSET:
            field_dict["escalationAction"] = escalation_action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        step_order = d.pop("stepOrder")

        step_name = d.pop("stepName")

        enable_escalation = d.pop("enableEscalation")

        escalation_time = d.pop("escalationTime")

        step_resolved = d.pop("stepResolved")

        escalation_action = d.pop("escalationAction", UNSET)

        workflow_step_update_form = cls(
            step_order=step_order,
            step_name=step_name,
            enable_escalation=enable_escalation,
            escalation_time=escalation_time,
            step_resolved=step_resolved,
            escalation_action=escalation_action,
        )

        workflow_step_update_form.additional_properties = d
        return workflow_step_update_form

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
