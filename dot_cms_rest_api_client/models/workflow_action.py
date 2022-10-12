from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.workflow_action_show_on_item import WorkflowActionShowOnItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowAction")


@attr.s(auto_attribs=True)
class WorkflowAction:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        scheme_id (Union[Unset, str]):
        condition (Union[Unset, str]):
        next_step (Union[Unset, str]):
        next_assign (Union[Unset, str]):
        icon (Union[Unset, str]):
        role_hierarchy_for_assign (Union[Unset, bool]):
        assignable (Union[Unset, bool]):
        commentable (Union[Unset, bool]):
        order (Union[Unset, int]):
        save_actionlet (Union[Unset, bool]):
        publish_actionlet (Union[Unset, bool]):
        unpublish_actionlet (Union[Unset, bool]):
        archive_actionlet (Union[Unset, bool]):
        push_publish_actionlet (Union[Unset, bool]):
        unarchive_actionlet (Union[Unset, bool]):
        delete_actionlet (Union[Unset, bool]):
        destroy_actionlet (Union[Unset, bool]):
        move_actionlet (Union[Unset, bool]):
        owner (Union[Unset, str]):
        move_actionlet_hash_path (Union[Unset, bool]):
        next_step_current_step (Union[Unset, bool]):
        show_on (Union[Unset, List[WorkflowActionShowOnItem]]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    scheme_id: Union[Unset, str] = UNSET
    condition: Union[Unset, str] = UNSET
    next_step: Union[Unset, str] = UNSET
    next_assign: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    role_hierarchy_for_assign: Union[Unset, bool] = UNSET
    assignable: Union[Unset, bool] = UNSET
    commentable: Union[Unset, bool] = UNSET
    order: Union[Unset, int] = UNSET
    save_actionlet: Union[Unset, bool] = UNSET
    publish_actionlet: Union[Unset, bool] = UNSET
    unpublish_actionlet: Union[Unset, bool] = UNSET
    archive_actionlet: Union[Unset, bool] = UNSET
    push_publish_actionlet: Union[Unset, bool] = UNSET
    unarchive_actionlet: Union[Unset, bool] = UNSET
    delete_actionlet: Union[Unset, bool] = UNSET
    destroy_actionlet: Union[Unset, bool] = UNSET
    move_actionlet: Union[Unset, bool] = UNSET
    owner: Union[Unset, str] = UNSET
    move_actionlet_hash_path: Union[Unset, bool] = UNSET
    next_step_current_step: Union[Unset, bool] = UNSET
    show_on: Union[Unset, List[WorkflowActionShowOnItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        scheme_id = self.scheme_id
        condition = self.condition
        next_step = self.next_step
        next_assign = self.next_assign
        icon = self.icon
        role_hierarchy_for_assign = self.role_hierarchy_for_assign
        assignable = self.assignable
        commentable = self.commentable
        order = self.order
        save_actionlet = self.save_actionlet
        publish_actionlet = self.publish_actionlet
        unpublish_actionlet = self.unpublish_actionlet
        archive_actionlet = self.archive_actionlet
        push_publish_actionlet = self.push_publish_actionlet
        unarchive_actionlet = self.unarchive_actionlet
        delete_actionlet = self.delete_actionlet
        destroy_actionlet = self.destroy_actionlet
        move_actionlet = self.move_actionlet
        owner = self.owner
        move_actionlet_hash_path = self.move_actionlet_hash_path
        next_step_current_step = self.next_step_current_step
        show_on: Union[Unset, List[str]] = UNSET
        if not isinstance(self.show_on, Unset):
            show_on = []
            for show_on_item_data in self.show_on:
                show_on_item = show_on_item_data.value

                show_on.append(show_on_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if scheme_id is not UNSET:
            field_dict["schemeId"] = scheme_id
        if condition is not UNSET:
            field_dict["condition"] = condition
        if next_step is not UNSET:
            field_dict["nextStep"] = next_step
        if next_assign is not UNSET:
            field_dict["nextAssign"] = next_assign
        if icon is not UNSET:
            field_dict["icon"] = icon
        if role_hierarchy_for_assign is not UNSET:
            field_dict["roleHierarchyForAssign"] = role_hierarchy_for_assign
        if assignable is not UNSET:
            field_dict["assignable"] = assignable
        if commentable is not UNSET:
            field_dict["commentable"] = commentable
        if order is not UNSET:
            field_dict["order"] = order
        if save_actionlet is not UNSET:
            field_dict["saveActionlet"] = save_actionlet
        if publish_actionlet is not UNSET:
            field_dict["publishActionlet"] = publish_actionlet
        if unpublish_actionlet is not UNSET:
            field_dict["unpublishActionlet"] = unpublish_actionlet
        if archive_actionlet is not UNSET:
            field_dict["archiveActionlet"] = archive_actionlet
        if push_publish_actionlet is not UNSET:
            field_dict["pushPublishActionlet"] = push_publish_actionlet
        if unarchive_actionlet is not UNSET:
            field_dict["unarchiveActionlet"] = unarchive_actionlet
        if delete_actionlet is not UNSET:
            field_dict["deleteActionlet"] = delete_actionlet
        if destroy_actionlet is not UNSET:
            field_dict["destroyActionlet"] = destroy_actionlet
        if move_actionlet is not UNSET:
            field_dict["moveActionlet"] = move_actionlet
        if owner is not UNSET:
            field_dict["owner"] = owner
        if move_actionlet_hash_path is not UNSET:
            field_dict["moveActionletHashPath"] = move_actionlet_hash_path
        if next_step_current_step is not UNSET:
            field_dict["nextStepCurrentStep"] = next_step_current_step
        if show_on is not UNSET:
            field_dict["showOn"] = show_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        scheme_id = d.pop("schemeId", UNSET)

        condition = d.pop("condition", UNSET)

        next_step = d.pop("nextStep", UNSET)

        next_assign = d.pop("nextAssign", UNSET)

        icon = d.pop("icon", UNSET)

        role_hierarchy_for_assign = d.pop("roleHierarchyForAssign", UNSET)

        assignable = d.pop("assignable", UNSET)

        commentable = d.pop("commentable", UNSET)

        order = d.pop("order", UNSET)

        save_actionlet = d.pop("saveActionlet", UNSET)

        publish_actionlet = d.pop("publishActionlet", UNSET)

        unpublish_actionlet = d.pop("unpublishActionlet", UNSET)

        archive_actionlet = d.pop("archiveActionlet", UNSET)

        push_publish_actionlet = d.pop("pushPublishActionlet", UNSET)

        unarchive_actionlet = d.pop("unarchiveActionlet", UNSET)

        delete_actionlet = d.pop("deleteActionlet", UNSET)

        destroy_actionlet = d.pop("destroyActionlet", UNSET)

        move_actionlet = d.pop("moveActionlet", UNSET)

        owner = d.pop("owner", UNSET)

        move_actionlet_hash_path = d.pop("moveActionletHashPath", UNSET)

        next_step_current_step = d.pop("nextStepCurrentStep", UNSET)

        show_on = []
        _show_on = d.pop("showOn", UNSET)
        for show_on_item_data in _show_on or []:
            show_on_item = WorkflowActionShowOnItem(show_on_item_data)

            show_on.append(show_on_item)

        workflow_action = cls(
            id=id,
            name=name,
            scheme_id=scheme_id,
            condition=condition,
            next_step=next_step,
            next_assign=next_assign,
            icon=icon,
            role_hierarchy_for_assign=role_hierarchy_for_assign,
            assignable=assignable,
            commentable=commentable,
            order=order,
            save_actionlet=save_actionlet,
            publish_actionlet=publish_actionlet,
            unpublish_actionlet=unpublish_actionlet,
            archive_actionlet=archive_actionlet,
            push_publish_actionlet=push_publish_actionlet,
            unarchive_actionlet=unarchive_actionlet,
            delete_actionlet=delete_actionlet,
            destroy_actionlet=destroy_actionlet,
            move_actionlet=move_actionlet,
            owner=owner,
            move_actionlet_hash_path=move_actionlet_hash_path,
            next_step_current_step=next_step_current_step,
            show_on=show_on,
        )

        workflow_action.additional_properties = d
        return workflow_action

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
