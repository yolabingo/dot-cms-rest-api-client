from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.workflow_actionlet_parameter import WorkflowActionletParameter
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkFlowActionlet")


@attr.s(auto_attribs=True)
class WorkFlowActionlet:
    """
    Attributes:
        localized_name (Union[Unset, str]):
        localized_howto (Union[Unset, str]):
        how_to (Union[Unset, str]):
        action_class (Union[Unset, str]):
        name (Union[Unset, str]):
        parameters (Union[Unset, List[WorkflowActionletParameter]]):
    """

    localized_name: Union[Unset, str] = UNSET
    localized_howto: Union[Unset, str] = UNSET
    how_to: Union[Unset, str] = UNSET
    action_class: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    parameters: Union[Unset, List[WorkflowActionletParameter]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        localized_name = self.localized_name
        localized_howto = self.localized_howto
        how_to = self.how_to
        action_class = self.action_class
        name = self.name
        parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()

                parameters.append(parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name
        if localized_howto is not UNSET:
            field_dict["localizedHowto"] = localized_howto
        if how_to is not UNSET:
            field_dict["howTo"] = how_to
        if action_class is not UNSET:
            field_dict["actionClass"] = action_class
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        localized_name = d.pop("localizedName", UNSET)

        localized_howto = d.pop("localizedHowto", UNSET)

        how_to = d.pop("howTo", UNSET)

        action_class = d.pop("actionClass", UNSET)

        name = d.pop("name", UNSET)

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = WorkflowActionletParameter.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        work_flow_actionlet = cls(
            localized_name=localized_name,
            localized_howto=localized_howto,
            how_to=how_to,
            action_class=action_class,
            name=name,
            parameters=parameters,
        )

        work_flow_actionlet.additional_properties = d
        return work_flow_actionlet

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
