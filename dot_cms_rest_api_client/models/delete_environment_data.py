from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteEnvironmentData")


@attr.s(auto_attribs=True)
class DeleteEnvironmentData:
    """
    Attributes:
        user (Union[Unset, str]):
        password (Union[Unset, str]):
        environment (Union[Unset, str]):
        type (Union[Unset, str]):
        callback (Union[Unset, str]):
    """

    user: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    callback: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user
        password = self.password
        environment = self.environment
        type = self.type
        callback = self.callback

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if password is not UNSET:
            field_dict["password"] = password
        if environment is not UNSET:
            field_dict["environment"] = environment
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

        environment = d.pop("environment", UNSET)

        type = d.pop("type", UNSET)

        callback = d.pop("callback", UNSET)

        delete_environment_data = cls(
            user=user,
            password=password,
            environment=environment,
            type=type,
            callback=callback,
        )

        delete_environment_data.additional_properties = d
        return delete_environment_data

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
