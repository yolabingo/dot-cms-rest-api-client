from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeletePPQueueElementsByIdentifierForm")


@attr.s(auto_attribs=True)
class DeletePPQueueElementsByIdentifierForm:
    """
    Attributes:
        identifiers (Union[Unset, List[str]]):
    """

    identifiers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifiers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = self.identifiers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifiers = cast(List[str], d.pop("identifiers", UNSET))

        delete_pp_queue_elements_by_identifier_form = cls(
            identifiers=identifiers,
        )

        delete_pp_queue_elements_by_identifier_form.additional_properties = d
        return delete_pp_queue_elements_by_identifier_form

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
