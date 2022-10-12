from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.workflow_system_action_form_system_action import WorkflowSystemActionFormSystemAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowSystemActionForm")


@attr.s(auto_attribs=True)
class WorkflowSystemActionForm:
    """
    Attributes:
        action_id (str):
        system_action (WorkflowSystemActionFormSystemAction):
        scheme_id (Union[Unset, str]):
        content_type_variable (Union[Unset, str]):
    """

    action_id: str
    system_action: WorkflowSystemActionFormSystemAction
    scheme_id: Union[Unset, str] = UNSET
    content_type_variable: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action_id = self.action_id
        system_action = self.system_action.value

        scheme_id = self.scheme_id
        content_type_variable = self.content_type_variable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionId": action_id,
                "systemAction": system_action,
            }
        )
        if scheme_id is not UNSET:
            field_dict["schemeId"] = scheme_id
        if content_type_variable is not UNSET:
            field_dict["contentTypeVariable"] = content_type_variable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action_id = d.pop("actionId")

        system_action = WorkflowSystemActionFormSystemAction(d.pop("systemAction"))

        scheme_id = d.pop("schemeId", UNSET)

        content_type_variable = d.pop("contentTypeVariable", UNSET)

        workflow_system_action_form = cls(
            action_id=action_id,
            system_action=system_action,
            scheme_id=scheme_id,
            content_type_variable=content_type_variable,
        )

        workflow_system_action_form.additional_properties = d
        return workflow_system_action_form

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
