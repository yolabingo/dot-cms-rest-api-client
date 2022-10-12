from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.additional_params_bean import AdditionalParamsBean
from ..types import UNSET, Unset

T = TypeVar("T", bound="FireBulkActionsForm")


@attr.s(auto_attribs=True)
class FireBulkActionsForm:
    """
    Attributes:
        query (Union[Unset, str]):
        contentlet_ids (Union[Unset, List[str]]):
        workflow_action_id (Union[Unset, str]):
        additional_params (Union[Unset, AdditionalParamsBean]):
        popup_params_bean (Union[Unset, AdditionalParamsBean]):
    """

    query: Union[Unset, str] = UNSET
    contentlet_ids: Union[Unset, List[str]] = UNSET
    workflow_action_id: Union[Unset, str] = UNSET
    additional_params: Union[Unset, AdditionalParamsBean] = UNSET
    popup_params_bean: Union[Unset, AdditionalParamsBean] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query
        contentlet_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contentlet_ids, Unset):
            contentlet_ids = self.contentlet_ids

        workflow_action_id = self.workflow_action_id
        additional_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_params, Unset):
            additional_params = self.additional_params.to_dict()

        popup_params_bean: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.popup_params_bean, Unset):
            popup_params_bean = self.popup_params_bean.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if contentlet_ids is not UNSET:
            field_dict["contentletIds"] = contentlet_ids
        if workflow_action_id is not UNSET:
            field_dict["workflowActionId"] = workflow_action_id
        if additional_params is not UNSET:
            field_dict["additionalParams"] = additional_params
        if popup_params_bean is not UNSET:
            field_dict["popupParamsBean"] = popup_params_bean

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query = d.pop("query", UNSET)

        contentlet_ids = cast(List[str], d.pop("contentletIds", UNSET))

        workflow_action_id = d.pop("workflowActionId", UNSET)

        _additional_params = d.pop("additionalParams", UNSET)
        additional_params: Union[Unset, AdditionalParamsBean]
        if isinstance(_additional_params, Unset):
            additional_params = UNSET
        else:
            additional_params = AdditionalParamsBean.from_dict(_additional_params)

        _popup_params_bean = d.pop("popupParamsBean", UNSET)
        popup_params_bean: Union[Unset, AdditionalParamsBean]
        if isinstance(_popup_params_bean, Unset):
            popup_params_bean = UNSET
        else:
            popup_params_bean = AdditionalParamsBean.from_dict(_popup_params_bean)

        fire_bulk_actions_form = cls(
            query=query,
            contentlet_ids=contentlet_ids,
            workflow_action_id=workflow_action_id,
            additional_params=additional_params,
            popup_params_bean=popup_params_bean,
        )

        fire_bulk_actions_form.additional_properties = d
        return fire_bulk_actions_form

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
