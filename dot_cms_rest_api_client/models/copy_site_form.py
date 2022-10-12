from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.site_form import SiteForm
from ..types import UNSET, Unset

T = TypeVar("T", bound="CopySiteForm")


@attr.s(auto_attribs=True)
class CopySiteForm:
    """
    Attributes:
        copy_from_site_id (Union[Unset, str]):
        copy_all (Union[Unset, bool]):
        copy_templates_containers (Union[Unset, bool]):
        copy_content_on_pages (Union[Unset, bool]):
        copy_folders (Union[Unset, bool]):
        copy_content_on_site (Union[Unset, bool]):
        copy_links (Union[Unset, bool]):
        copy_site_variables (Union[Unset, bool]):
        site (Union[Unset, SiteForm]):
    """

    copy_from_site_id: Union[Unset, str] = UNSET
    copy_all: Union[Unset, bool] = UNSET
    copy_templates_containers: Union[Unset, bool] = UNSET
    copy_content_on_pages: Union[Unset, bool] = UNSET
    copy_folders: Union[Unset, bool] = UNSET
    copy_content_on_site: Union[Unset, bool] = UNSET
    copy_links: Union[Unset, bool] = UNSET
    copy_site_variables: Union[Unset, bool] = UNSET
    site: Union[Unset, SiteForm] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        copy_from_site_id = self.copy_from_site_id
        copy_all = self.copy_all
        copy_templates_containers = self.copy_templates_containers
        copy_content_on_pages = self.copy_content_on_pages
        copy_folders = self.copy_folders
        copy_content_on_site = self.copy_content_on_site
        copy_links = self.copy_links
        copy_site_variables = self.copy_site_variables
        site: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if copy_from_site_id is not UNSET:
            field_dict["copyFromSiteId"] = copy_from_site_id
        if copy_all is not UNSET:
            field_dict["copyAll"] = copy_all
        if copy_templates_containers is not UNSET:
            field_dict["copyTemplatesContainers"] = copy_templates_containers
        if copy_content_on_pages is not UNSET:
            field_dict["copyContentOnPages"] = copy_content_on_pages
        if copy_folders is not UNSET:
            field_dict["copyFolders"] = copy_folders
        if copy_content_on_site is not UNSET:
            field_dict["copyContentOnSite"] = copy_content_on_site
        if copy_links is not UNSET:
            field_dict["copyLinks"] = copy_links
        if copy_site_variables is not UNSET:
            field_dict["copySiteVariables"] = copy_site_variables
        if site is not UNSET:
            field_dict["site"] = site

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        copy_from_site_id = d.pop("copyFromSiteId", UNSET)

        copy_all = d.pop("copyAll", UNSET)

        copy_templates_containers = d.pop("copyTemplatesContainers", UNSET)

        copy_content_on_pages = d.pop("copyContentOnPages", UNSET)

        copy_folders = d.pop("copyFolders", UNSET)

        copy_content_on_site = d.pop("copyContentOnSite", UNSET)

        copy_links = d.pop("copyLinks", UNSET)

        copy_site_variables = d.pop("copySiteVariables", UNSET)

        _site = d.pop("site", UNSET)
        site: Union[Unset, SiteForm]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = SiteForm.from_dict(_site)

        copy_site_form = cls(
            copy_from_site_id=copy_from_site_id,
            copy_all=copy_all,
            copy_templates_containers=copy_templates_containers,
            copy_content_on_pages=copy_content_on_pages,
            copy_folders=copy_folders,
            copy_content_on_site=copy_content_on_site,
            copy_links=copy_links,
            copy_site_variables=copy_site_variables,
            site=site,
        )

        copy_site_form.additional_properties = d
        return copy_site_form

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
