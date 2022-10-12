from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="WorkflowActionStepForm")


@attr.s(auto_attribs=True)
class WorkflowActionStepForm:
    """
    Attributes:
        action_id (str):
    """

    action_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action_id = self.action_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionId": action_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action_id = d.pop("actionId")

        workflow_action_step_form = cls(
            action_id=action_id,
        )

        workflow_action_step_form.additional_properties = d
        return workflow_action_step_form

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
