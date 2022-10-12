from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowActionletParameter")


@attr.s(auto_attribs=True)
class WorkflowActionletParameter:
    """
    Attributes:
        display_name (Union[Unset, str]):
        key (Union[Unset, str]):
        default_value (Union[Unset, str]):
        required (Union[Unset, bool]):
    """

    display_name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        key = self.key
        default_value = self.default_value
        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if key is not UNSET:
            field_dict["key"] = key
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        key = d.pop("key", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        required = d.pop("required", UNSET)

        workflow_actionlet_parameter = cls(
            display_name=display_name,
            key=key,
            default_value=default_value,
            required=required,
        )

        workflow_actionlet_parameter.additional_properties = d
        return workflow_actionlet_parameter

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
