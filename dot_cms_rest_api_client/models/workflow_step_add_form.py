from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="WorkflowStepAddForm")


@attr.s(auto_attribs=True)
class WorkflowStepAddForm:
    """
    Attributes:
        scheme_id (str):
        step_name (str):
        enable_escalation (bool):
        escalation_action (str):
        escalation_time (str):
        step_resolved (bool):
    """

    scheme_id: str
    step_name: str
    enable_escalation: bool
    escalation_action: str
    escalation_time: str
    step_resolved: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheme_id = self.scheme_id
        step_name = self.step_name
        enable_escalation = self.enable_escalation
        escalation_action = self.escalation_action
        escalation_time = self.escalation_time
        step_resolved = self.step_resolved

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schemeId": scheme_id,
                "stepName": step_name,
                "enableEscalation": enable_escalation,
                "escalationAction": escalation_action,
                "escalationTime": escalation_time,
                "stepResolved": step_resolved,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scheme_id = d.pop("schemeId")

        step_name = d.pop("stepName")

        enable_escalation = d.pop("enableEscalation")

        escalation_action = d.pop("escalationAction")

        escalation_time = d.pop("escalationTime")

        step_resolved = d.pop("stepResolved")

        workflow_step_add_form = cls(
            scheme_id=scheme_id,
            step_name=step_name,
            enable_escalation=enable_escalation,
            escalation_action=escalation_action,
            escalation_time=escalation_time,
            step_resolved=step_resolved,
        )

        workflow_step_add_form.additional_properties = d
        return workflow_step_add_form

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
