from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.workflow_action_form_show_on_item import WorkflowActionFormShowOnItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowActionForm")


@attr.s(auto_attribs=True)
class WorkflowActionForm:
    """
    Attributes:
        scheme_id (str):
        action_name (str):
        action_assignable (bool):
        action_commentable (bool):
        requires_checkout (bool):
        show_on (List[WorkflowActionFormShowOnItem]):
        action_role_hierarchy_for_assign (bool):
        action_next_step (str):
        action_id (Union[Unset, str]):
        step_id (Union[Unset, str]):
        who_can_use (Union[Unset, List[str]]):
        action_icon (Union[Unset, str]):
        role_hierarchy_for_assign (Union[Unset, bool]):
        action_next_assign (Union[Unset, str]):
        action_condition (Union[Unset, str]):
    """

    scheme_id: str
    action_name: str
    action_assignable: bool
    action_commentable: bool
    requires_checkout: bool
    show_on: List[WorkflowActionFormShowOnItem]
    action_role_hierarchy_for_assign: bool
    action_next_step: str
    action_id: Union[Unset, str] = UNSET
    step_id: Union[Unset, str] = UNSET
    who_can_use: Union[Unset, List[str]] = UNSET
    action_icon: Union[Unset, str] = UNSET
    role_hierarchy_for_assign: Union[Unset, bool] = UNSET
    action_next_assign: Union[Unset, str] = UNSET
    action_condition: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheme_id = self.scheme_id
        action_name = self.action_name
        action_assignable = self.action_assignable
        action_commentable = self.action_commentable
        requires_checkout = self.requires_checkout
        show_on = []
        for show_on_item_data in self.show_on:
            show_on_item = show_on_item_data.value

            show_on.append(show_on_item)

        action_role_hierarchy_for_assign = self.action_role_hierarchy_for_assign
        action_next_step = self.action_next_step
        action_id = self.action_id
        step_id = self.step_id
        who_can_use: Union[Unset, List[str]] = UNSET
        if not isinstance(self.who_can_use, Unset):
            who_can_use = self.who_can_use

        action_icon = self.action_icon
        role_hierarchy_for_assign = self.role_hierarchy_for_assign
        action_next_assign = self.action_next_assign
        action_condition = self.action_condition

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schemeId": scheme_id,
                "actionName": action_name,
                "actionAssignable": action_assignable,
                "actionCommentable": action_commentable,
                "requiresCheckout": requires_checkout,
                "showOn": show_on,
                "actionRoleHierarchyForAssign": action_role_hierarchy_for_assign,
                "actionNextStep": action_next_step,
            }
        )
        if action_id is not UNSET:
            field_dict["actionId"] = action_id
        if step_id is not UNSET:
            field_dict["stepId"] = step_id
        if who_can_use is not UNSET:
            field_dict["whoCanUse"] = who_can_use
        if action_icon is not UNSET:
            field_dict["actionIcon"] = action_icon
        if role_hierarchy_for_assign is not UNSET:
            field_dict["roleHierarchyForAssign"] = role_hierarchy_for_assign
        if action_next_assign is not UNSET:
            field_dict["actionNextAssign"] = action_next_assign
        if action_condition is not UNSET:
            field_dict["actionCondition"] = action_condition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scheme_id = d.pop("schemeId")

        action_name = d.pop("actionName")

        action_assignable = d.pop("actionAssignable")

        action_commentable = d.pop("actionCommentable")

        requires_checkout = d.pop("requiresCheckout")

        show_on = []
        _show_on = d.pop("showOn")
        for show_on_item_data in _show_on:
            show_on_item = WorkflowActionFormShowOnItem(show_on_item_data)

            show_on.append(show_on_item)

        action_role_hierarchy_for_assign = d.pop("actionRoleHierarchyForAssign")

        action_next_step = d.pop("actionNextStep")

        action_id = d.pop("actionId", UNSET)

        step_id = d.pop("stepId", UNSET)

        who_can_use = cast(List[str], d.pop("whoCanUse", UNSET))

        action_icon = d.pop("actionIcon", UNSET)

        role_hierarchy_for_assign = d.pop("roleHierarchyForAssign", UNSET)

        action_next_assign = d.pop("actionNextAssign", UNSET)

        action_condition = d.pop("actionCondition", UNSET)

        workflow_action_form = cls(
            scheme_id=scheme_id,
            action_name=action_name,
            action_assignable=action_assignable,
            action_commentable=action_commentable,
            requires_checkout=requires_checkout,
            show_on=show_on,
            action_role_hierarchy_for_assign=action_role_hierarchy_for_assign,
            action_next_step=action_next_step,
            action_id=action_id,
            step_id=step_id,
            who_can_use=who_can_use,
            action_icon=action_icon,
            role_hierarchy_for_assign=role_hierarchy_for_assign,
            action_next_assign=action_next_assign,
            action_condition=action_condition,
        )

        workflow_action_form.additional_properties = d
        return workflow_action_form

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
