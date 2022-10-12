from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowSchemeForm")


@attr.s(auto_attribs=True)
class WorkflowSchemeForm:
    """
    Attributes:
        scheme_name (str):
        scheme_description (Union[Unset, str]):
        scheme_archived (Union[Unset, bool]):
    """

    scheme_name: str
    scheme_description: Union[Unset, str] = UNSET
    scheme_archived: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheme_name = self.scheme_name
        scheme_description = self.scheme_description
        scheme_archived = self.scheme_archived

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schemeName": scheme_name,
            }
        )
        if scheme_description is not UNSET:
            field_dict["schemeDescription"] = scheme_description
        if scheme_archived is not UNSET:
            field_dict["schemeArchived"] = scheme_archived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scheme_name = d.pop("schemeName")

        scheme_description = d.pop("schemeDescription", UNSET)

        scheme_archived = d.pop("schemeArchived", UNSET)

        workflow_scheme_form = cls(
            scheme_name=scheme_name,
            scheme_description=scheme_description,
            scheme_archived=scheme_archived,
        )

        workflow_scheme_form.additional_properties = d
        return workflow_scheme_form

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
