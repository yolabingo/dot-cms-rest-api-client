import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PageContentType")


@attr.s(auto_attribs=True)
class PageContentType:
    """
    Attributes:
        clazz (str):
        owner (Union[Unset, str]):
        name (Union[Unset, str]):
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        default_type (Union[Unset, bool]):
        detail_page (Union[Unset, str]):
        fixed (Union[Unset, bool]):
        i_date (Union[Unset, datetime.datetime]):
        system (Union[Unset, bool]):
        versionable (Union[Unset, bool]):
        multilingualable (Union[Unset, bool]):
        variable (Union[Unset, str]):
        url_map_pattern (Union[Unset, str]):
        publish_date_var (Union[Unset, str]):
        expire_date_var (Union[Unset, str]):
        mod_date (Union[Unset, datetime.datetime]):
        host (Union[Unset, str]):
        icon (Union[Unset, str]):
        sort_order (Union[Unset, int]):
        folder (Union[Unset, str]):
    """

    clazz: str
    owner: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    default_type: Union[Unset, bool] = UNSET
    detail_page: Union[Unset, str] = UNSET
    fixed: Union[Unset, bool] = UNSET
    i_date: Union[Unset, datetime.datetime] = UNSET
    system: Union[Unset, bool] = UNSET
    versionable: Union[Unset, bool] = UNSET
    multilingualable: Union[Unset, bool] = UNSET
    variable: Union[Unset, str] = UNSET
    url_map_pattern: Union[Unset, str] = UNSET
    publish_date_var: Union[Unset, str] = UNSET
    expire_date_var: Union[Unset, str] = UNSET
    mod_date: Union[Unset, datetime.datetime] = UNSET
    host: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET
    folder: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clazz = self.clazz
        owner = self.owner
        name = self.name
        id = self.id
        description = self.description
        default_type = self.default_type
        detail_page = self.detail_page
        fixed = self.fixed
        i_date: Union[Unset, str] = UNSET
        if not isinstance(self.i_date, Unset):
            i_date = self.i_date.isoformat()

        system = self.system
        versionable = self.versionable
        multilingualable = self.multilingualable
        variable = self.variable
        url_map_pattern = self.url_map_pattern
        publish_date_var = self.publish_date_var
        expire_date_var = self.expire_date_var
        mod_date: Union[Unset, str] = UNSET
        if not isinstance(self.mod_date, Unset):
            mod_date = self.mod_date.isoformat()

        host = self.host
        icon = self.icon
        sort_order = self.sort_order
        folder = self.folder

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clazz": clazz,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if default_type is not UNSET:
            field_dict["defaultType"] = default_type
        if detail_page is not UNSET:
            field_dict["detailPage"] = detail_page
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if i_date is not UNSET:
            field_dict["iDate"] = i_date
        if system is not UNSET:
            field_dict["system"] = system
        if versionable is not UNSET:
            field_dict["versionable"] = versionable
        if multilingualable is not UNSET:
            field_dict["multilingualable"] = multilingualable
        if variable is not UNSET:
            field_dict["variable"] = variable
        if url_map_pattern is not UNSET:
            field_dict["urlMapPattern"] = url_map_pattern
        if publish_date_var is not UNSET:
            field_dict["publishDateVar"] = publish_date_var
        if expire_date_var is not UNSET:
            field_dict["expireDateVar"] = expire_date_var
        if mod_date is not UNSET:
            field_dict["modDate"] = mod_date
        if host is not UNSET:
            field_dict["host"] = host
        if icon is not UNSET:
            field_dict["icon"] = icon
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clazz = d.pop("clazz")

        owner = d.pop("owner", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        default_type = d.pop("defaultType", UNSET)

        detail_page = d.pop("detailPage", UNSET)

        fixed = d.pop("fixed", UNSET)

        _i_date = d.pop("iDate", UNSET)
        i_date: Union[Unset, datetime.datetime]
        if isinstance(_i_date, Unset):
            i_date = UNSET
        else:
            i_date = isoparse(_i_date)

        system = d.pop("system", UNSET)

        versionable = d.pop("versionable", UNSET)

        multilingualable = d.pop("multilingualable", UNSET)

        variable = d.pop("variable", UNSET)

        url_map_pattern = d.pop("urlMapPattern", UNSET)

        publish_date_var = d.pop("publishDateVar", UNSET)

        expire_date_var = d.pop("expireDateVar", UNSET)

        _mod_date = d.pop("modDate", UNSET)
        mod_date: Union[Unset, datetime.datetime]
        if isinstance(_mod_date, Unset):
            mod_date = UNSET
        else:
            mod_date = isoparse(_mod_date)

        host = d.pop("host", UNSET)

        icon = d.pop("icon", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        folder = d.pop("folder", UNSET)

        page_content_type = cls(
            clazz=clazz,
            owner=owner,
            name=name,
            id=id,
            description=description,
            default_type=default_type,
            detail_page=detail_page,
            fixed=fixed,
            i_date=i_date,
            system=system,
            versionable=versionable,
            multilingualable=multilingualable,
            variable=variable,
            url_map_pattern=url_map_pattern,
            publish_date_var=publish_date_var,
            expire_date_var=expire_date_var,
            mod_date=mod_date,
            host=host,
            icon=icon,
            sort_order=sort_order,
            folder=folder,
        )

        page_content_type.additional_properties = d
        return page_content_type

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
