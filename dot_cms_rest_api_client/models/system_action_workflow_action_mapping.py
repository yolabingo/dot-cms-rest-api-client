from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.system_action_workflow_action_mapping_owner import SystemActionWorkflowActionMappingOwner
from ..models.system_action_workflow_action_mapping_system_action import SystemActionWorkflowActionMappingSystemAction
from ..models.workflow_action import WorkflowAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemActionWorkflowActionMapping")


@attr.s(auto_attribs=True)
class SystemActionWorkflowActionMapping:
    """
    Attributes:
        identifier (Union[Unset, str]):
        system_action (Union[Unset, SystemActionWorkflowActionMappingSystemAction]):
        workflow_action (Union[Unset, WorkflowAction]):
        owner (Union[Unset, SystemActionWorkflowActionMappingOwner]):
        owner_content_type (Union[Unset, bool]):
        owner_scheme (Union[Unset, bool]):
    """

    identifier: Union[Unset, str] = UNSET
    system_action: Union[Unset, SystemActionWorkflowActionMappingSystemAction] = UNSET
    workflow_action: Union[Unset, WorkflowAction] = UNSET
    owner: Union[Unset, SystemActionWorkflowActionMappingOwner] = UNSET
    owner_content_type: Union[Unset, bool] = UNSET
    owner_scheme: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        system_action: Union[Unset, str] = UNSET
        if not isinstance(self.system_action, Unset):
            system_action = self.system_action.value

        workflow_action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_action, Unset):
            workflow_action = self.workflow_action.to_dict()

        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        owner_content_type = self.owner_content_type
        owner_scheme = self.owner_scheme

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if system_action is not UNSET:
            field_dict["systemAction"] = system_action
        if workflow_action is not UNSET:
            field_dict["workflowAction"] = workflow_action
        if owner is not UNSET:
            field_dict["owner"] = owner
        if owner_content_type is not UNSET:
            field_dict["ownerContentType"] = owner_content_type
        if owner_scheme is not UNSET:
            field_dict["ownerScheme"] = owner_scheme

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier", UNSET)

        _system_action = d.pop("systemAction", UNSET)
        system_action: Union[Unset, SystemActionWorkflowActionMappingSystemAction]
        if isinstance(_system_action, Unset):
            system_action = UNSET
        else:
            system_action = SystemActionWorkflowActionMappingSystemAction(_system_action)

        _workflow_action = d.pop("workflowAction", UNSET)
        workflow_action: Union[Unset, WorkflowAction]
        if isinstance(_workflow_action, Unset):
            workflow_action = UNSET
        else:
            workflow_action = WorkflowAction.from_dict(_workflow_action)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, SystemActionWorkflowActionMappingOwner]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = SystemActionWorkflowActionMappingOwner.from_dict(_owner)

        owner_content_type = d.pop("ownerContentType", UNSET)

        owner_scheme = d.pop("ownerScheme", UNSET)

        system_action_workflow_action_mapping = cls(
            identifier=identifier,
            system_action=system_action,
            workflow_action=workflow_action,
            owner=owner,
            owner_content_type=owner_content_type,
            owner_scheme=owner_scheme,
        )

        system_action_workflow_action_mapping.additional_properties = d
        return system_action_workflow_action_mapping

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
