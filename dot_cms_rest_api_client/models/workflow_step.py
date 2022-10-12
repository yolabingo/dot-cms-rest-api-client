import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowStep")


@attr.s(auto_attribs=True)
class WorkflowStep:
    """
    Attributes:
        id (Union[Unset, str]):
        creation_date (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        scheme_id (Union[Unset, str]):
        my_order (Union[Unset, int]):
        resolved (Union[Unset, bool]):
        enable_escalation (Union[Unset, bool]):
        escalation_action (Union[Unset, str]):
        escalation_time (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    scheme_id: Union[Unset, str] = UNSET
    my_order: Union[Unset, int] = UNSET
    resolved: Union[Unset, bool] = UNSET
    enable_escalation: Union[Unset, bool] = UNSET
    escalation_action: Union[Unset, str] = UNSET
    escalation_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        name = self.name
        scheme_id = self.scheme_id
        my_order = self.my_order
        resolved = self.resolved
        enable_escalation = self.enable_escalation
        escalation_action = self.escalation_action
        escalation_time = self.escalation_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if name is not UNSET:
            field_dict["name"] = name
        if scheme_id is not UNSET:
            field_dict["schemeId"] = scheme_id
        if my_order is not UNSET:
            field_dict["myOrder"] = my_order
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if enable_escalation is not UNSET:
            field_dict["enableEscalation"] = enable_escalation
        if escalation_action is not UNSET:
            field_dict["escalationAction"] = escalation_action
        if escalation_time is not UNSET:
            field_dict["escalationTime"] = escalation_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        name = d.pop("name", UNSET)

        scheme_id = d.pop("schemeId", UNSET)

        my_order = d.pop("myOrder", UNSET)

        resolved = d.pop("resolved", UNSET)

        enable_escalation = d.pop("enableEscalation", UNSET)

        escalation_action = d.pop("escalationAction", UNSET)

        escalation_time = d.pop("escalationTime", UNSET)

        workflow_step = cls(
            id=id,
            creation_date=creation_date,
            name=name,
            scheme_id=scheme_id,
            my_order=my_order,
            resolved=resolved,
            enable_escalation=enable_escalation,
            escalation_action=escalation_action,
            escalation_time=escalation_time,
        )

        workflow_step.additional_properties = d
        return workflow_step

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
