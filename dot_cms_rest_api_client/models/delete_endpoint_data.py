from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteEndpointData")


@attr.s(auto_attribs=True)
class DeleteEndpointData:
    """
    Attributes:
        user (Union[Unset, str]):
        password (Union[Unset, str]):
        end_point (Union[Unset, str]):
        type (Union[Unset, str]):
        callback (Union[Unset, str]):
    """

    user: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    end_point: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    callback: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user
        password = self.password
        end_point = self.end_point
        type = self.type
        callback = self.callback

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if password is not UNSET:
            field_dict["password"] = password
        if end_point is not UNSET:
            field_dict["endPoint"] = end_point
        if type is not UNSET:
            field_dict["type"] = type
        if callback is not UNSET:
            field_dict["callback"] = callback

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user", UNSET)

        password = d.pop("password", UNSET)

        end_point = d.pop("endPoint", UNSET)

        type = d.pop("type", UNSET)

        callback = d.pop("callback", UNSET)

        delete_endpoint_data = cls(
            user=user,
            password=password,
            end_point=end_point,
            type=type,
            callback=callback,
        )

        delete_endpoint_data.additional_properties = d
        return delete_endpoint_data

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
