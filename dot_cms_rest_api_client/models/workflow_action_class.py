from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.work_flow_actionlet import WorkFlowActionlet
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowActionClass")


@attr.s(auto_attribs=True)
class WorkflowActionClass:
    """
    Attributes:
        id (Union[Unset, str]):
        action_id (Union[Unset, str]):
        name (Union[Unset, str]):
        order (Union[Unset, int]):
        clazz (Union[Unset, str]):
        actionlet (Union[Unset, WorkFlowActionlet]):
    """

    id: Union[Unset, str] = UNSET
    action_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    clazz: Union[Unset, str] = UNSET
    actionlet: Union[Unset, WorkFlowActionlet] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        action_id = self.action_id
        name = self.name
        order = self.order
        clazz = self.clazz
        actionlet: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actionlet, Unset):
            actionlet = self.actionlet.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if action_id is not UNSET:
            field_dict["actionId"] = action_id
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if clazz is not UNSET:
            field_dict["clazz"] = clazz
        if actionlet is not UNSET:
            field_dict["actionlet"] = actionlet

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        action_id = d.pop("actionId", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        clazz = d.pop("clazz", UNSET)

        _actionlet = d.pop("actionlet", UNSET)
        actionlet: Union[Unset, WorkFlowActionlet]
        if isinstance(_actionlet, Unset):
            actionlet = UNSET
        else:
            actionlet = WorkFlowActionlet.from_dict(_actionlet)

        workflow_action_class = cls(
            id=id,
            action_id=action_id,
            name=name,
            order=order,
            clazz=clazz,
            actionlet=actionlet,
        )

        workflow_action_class.additional_properties = d
        return workflow_action_class

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
