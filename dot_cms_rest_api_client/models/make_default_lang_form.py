from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MakeDefaultLangForm")


@attr.s(auto_attribs=True)
class MakeDefaultLangForm:
    """
    Attributes:
        fire_transfer_assets_job (Union[Unset, bool]):
    """

    fire_transfer_assets_job: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fire_transfer_assets_job = self.fire_transfer_assets_job

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fire_transfer_assets_job is not UNSET:
            field_dict["fireTransferAssetsJob"] = fire_transfer_assets_job

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fire_transfer_assets_job = d.pop("fireTransferAssetsJob", UNSET)

        make_default_lang_form = cls(
            fire_transfer_assets_job=fire_transfer_assets_job,
        )

        make_default_lang_form.additional_properties = d
        return make_default_lang_form

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
