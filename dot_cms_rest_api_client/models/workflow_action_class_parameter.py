from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowActionClassParameter")


@attr.s(auto_attribs=True)
class WorkflowActionClassParameter:
    """
    Attributes:
        id (Union[Unset, str]):
        action_class_id (Union[Unset, str]):
        key (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    action_class_id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        action_class_id = self.action_class_id
        key = self.key
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if action_class_id is not UNSET:
            field_dict["actionClassId"] = action_class_id
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        action_class_id = d.pop("actionClassId", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        workflow_action_class_parameter = cls(
            id=id,
            action_class_id=action_class_id,
            key=key,
            value=value,
        )

        workflow_action_class_parameter.additional_properties = d
        return workflow_action_class_parameter

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
