from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.parameterized_header_parameters import ParameterizedHeaderParameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParameterizedHeader")


@attr.s(auto_attribs=True)
class ParameterizedHeader:
    """
    Attributes:
        value (Union[Unset, str]):
        parameters (Union[Unset, ParameterizedHeaderParameters]):
    """

    value: Union[Unset, str] = UNSET
    parameters: Union[Unset, ParameterizedHeaderParameters] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, ParameterizedHeaderParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ParameterizedHeaderParameters.from_dict(_parameters)

        parameterized_header = cls(
            value=value,
            parameters=parameters,
        )

        parameterized_header.additional_properties = d
        return parameterized_header

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
