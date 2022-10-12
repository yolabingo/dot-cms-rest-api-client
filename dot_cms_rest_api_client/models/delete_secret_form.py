from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="DeleteSecretForm")


@attr.s(auto_attribs=True)
class DeleteSecretForm:
    """
    Attributes:
        key (str):
        site_id (str):
        params (List[str]):
    """

    key: str
    site_id: str
    params: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        site_id = self.site_id
        params = self.params

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "siteId": site_id,
                "params": params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        site_id = d.pop("siteId")

        params = cast(List[str], d.pop("params"))

        delete_secret_form = cls(
            key=key,
            site_id=site_id,
            params=params,
        )

        delete_secret_form.additional_properties = d
        return delete_secret_form

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
