from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.generate_bundle_form_operation import GenerateBundleFormOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateBundleForm")


@attr.s(auto_attribs=True)
class GenerateBundleForm:
    """
    Attributes:
        bundle_id (Union[Unset, str]):
        operation (Union[Unset, GenerateBundleFormOperation]):
        filter_key (Union[Unset, str]):
    """

    bundle_id: Union[Unset, str] = UNSET
    operation: Union[Unset, GenerateBundleFormOperation] = UNSET
    filter_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bundle_id = self.bundle_id
        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        filter_key = self.filter_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if filter_key is not UNSET:
            field_dict["filterKey"] = filter_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bundle_id = d.pop("bundleId", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, GenerateBundleFormOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = GenerateBundleFormOperation(_operation)

        filter_key = d.pop("filterKey", UNSET)

        generate_bundle_form = cls(
            bundle_id=bundle_id,
            operation=operation,
            filter_key=filter_key,
        )

        generate_bundle_form.additional_properties = d
        return generate_bundle_form

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
