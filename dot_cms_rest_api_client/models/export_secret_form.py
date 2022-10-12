from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.export_secret_form_app_keys import ExportSecretFormAppKeys
from ..models.export_secret_form_app_keys_by_site import ExportSecretFormAppKeysBySite
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportSecretForm")


@attr.s(auto_attribs=True)
class ExportSecretForm:
    """
    Attributes:
        password (str):
        export_all (bool):
        app_keys_by_site (ExportSecretFormAppKeysBySite):
        app_keys (Union[Unset, ExportSecretFormAppKeys]):
    """

    password: str
    export_all: bool
    app_keys_by_site: ExportSecretFormAppKeysBySite
    app_keys: Union[Unset, ExportSecretFormAppKeys] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        export_all = self.export_all
        app_keys_by_site = self.app_keys_by_site.to_dict()

        app_keys: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.app_keys, Unset):
            app_keys = self.app_keys.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
                "exportAll": export_all,
                "appKeysBySite": app_keys_by_site,
            }
        )
        if app_keys is not UNSET:
            field_dict["appKeys"] = app_keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password")

        export_all = d.pop("exportAll")

        app_keys_by_site = ExportSecretFormAppKeysBySite.from_dict(d.pop("appKeysBySite"))

        _app_keys = d.pop("appKeys", UNSET)
        app_keys: Union[Unset, ExportSecretFormAppKeys]
        if isinstance(_app_keys, Unset):
            app_keys = UNSET
        else:
            app_keys = ExportSecretFormAppKeys.from_dict(_app_keys)

        export_secret_form = cls(
            password=password,
            export_all=export_all,
            app_keys_by_site=app_keys_by_site,
            app_keys=app_keys,
        )

        export_secret_form.additional_properties = d
        return export_secret_form

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
