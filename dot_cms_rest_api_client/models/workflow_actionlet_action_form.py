from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.workflow_actionlet_action_form_parameters import WorkflowActionletActionFormParameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowActionletActionForm")


@attr.s(auto_attribs=True)
class WorkflowActionletActionForm:
    """
    Attributes:
        actionlet_class (str):
        order (Union[Unset, int]):
        parameters (Union[Unset, WorkflowActionletActionFormParameters]):
    """

    actionlet_class: str
    order: Union[Unset, int] = UNSET
    parameters: Union[Unset, WorkflowActionletActionFormParameters] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actionlet_class = self.actionlet_class
        order = self.order
        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionletClass": actionlet_class,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        actionlet_class = d.pop("actionletClass")

        order = d.pop("order", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, WorkflowActionletActionFormParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = WorkflowActionletActionFormParameters.from_dict(_parameters)

        workflow_actionlet_action_form = cls(
            actionlet_class=actionlet_class,
            order=order,
            parameters=parameters,
        )

        workflow_actionlet_action_form.additional_properties = d
        return workflow_actionlet_action_form

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
