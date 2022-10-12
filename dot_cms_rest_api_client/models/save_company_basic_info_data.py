from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveCompanyBasicInfoData")


@attr.s(auto_attribs=True)
class SaveCompanyBasicInfoData:
    """
    Attributes:
        user (Union[Unset, str]):
        password (Union[Unset, str]):
        portal_url (Union[Unset, str]):
        mx (Union[Unset, str]):
        email_address (Union[Unset, str]):
        size (Union[Unset, str]):
        type (Union[Unset, str]):
        street (Union[Unset, str]):
        home_url (Union[Unset, str]):
        city (Union[Unset, str]):
        state (Union[Unset, str]):
    """

    user: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    portal_url: Union[Unset, str] = UNSET
    mx: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    home_url: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user
        password = self.password
        portal_url = self.portal_url
        mx = self.mx
        email_address = self.email_address
        size = self.size
        type = self.type
        street = self.street
        home_url = self.home_url
        city = self.city
        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if password is not UNSET:
            field_dict["password"] = password
        if portal_url is not UNSET:
            field_dict["portalURL"] = portal_url
        if mx is not UNSET:
            field_dict["mx"] = mx
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if size is not UNSET:
            field_dict["size"] = size
        if type is not UNSET:
            field_dict["type"] = type
        if street is not UNSET:
            field_dict["street"] = street
        if home_url is not UNSET:
            field_dict["homeURL"] = home_url
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user", UNSET)

        password = d.pop("password", UNSET)

        portal_url = d.pop("portalURL", UNSET)

        mx = d.pop("mx", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        size = d.pop("size", UNSET)

        type = d.pop("type", UNSET)

        street = d.pop("street", UNSET)

        home_url = d.pop("homeURL", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        save_company_basic_info_data = cls(
            user=user,
            password=password,
            portal_url=portal_url,
            mx=mx,
            email_address=email_address,
            size=size,
            type=type,
            street=street,
            home_url=home_url,
            city=city,
            state=state,
        )

        save_company_basic_info_data.additional_properties = d
        return save_company_basic_info_data

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
