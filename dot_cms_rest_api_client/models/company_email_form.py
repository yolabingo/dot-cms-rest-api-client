from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyEmailForm")


@attr.s(auto_attribs=True)
class CompanyEmailForm:
    """
    Attributes:
        sender_and_email (Union[Unset, str]):
    """

    sender_and_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sender_and_email = self.sender_and_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sender_and_email is not UNSET:
            field_dict["senderAndEmail"] = sender_and_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sender_and_email = d.pop("senderAndEmail", UNSET)

        company_email_form = cls(
            sender_and_email=sender_and_email,
        )

        company_email_form.additional_properties = d
        return company_email_form

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
