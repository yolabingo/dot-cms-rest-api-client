from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteForm")


@attr.s(auto_attribs=True)
class SiteForm:
    """
    Attributes:
        aliases (Union[Unset, str]):
        site_name (Union[Unset, str]):
        tag_storage (Union[Unset, str]):
        site_thumbnail (Union[Unset, str]):
        run_dashboard (Union[Unset, bool]):
        keywords (Union[Unset, str]):
        description (Union[Unset, str]):
        google_map (Union[Unset, str]):
        google_analytics (Union[Unset, str]):
        add_this (Union[Unset, str]):
        proxy_url_for_edit_mode (Union[Unset, str]):
        embedded_dashboard (Union[Unset, str]):
        language_id (Union[Unset, int]):
        identifier (Union[Unset, str]):
        inode (Union[Unset, str]):
        force_execution (Union[Unset, bool]):
    """

    aliases: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    tag_storage: Union[Unset, str] = UNSET
    site_thumbnail: Union[Unset, str] = UNSET
    run_dashboard: Union[Unset, bool] = UNSET
    keywords: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    google_map: Union[Unset, str] = UNSET
    google_analytics: Union[Unset, str] = UNSET
    add_this: Union[Unset, str] = UNSET
    proxy_url_for_edit_mode: Union[Unset, str] = UNSET
    embedded_dashboard: Union[Unset, str] = UNSET
    language_id: Union[Unset, int] = UNSET
    identifier: Union[Unset, str] = UNSET
    inode: Union[Unset, str] = UNSET
    force_execution: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aliases = self.aliases
        site_name = self.site_name
        tag_storage = self.tag_storage
        site_thumbnail = self.site_thumbnail
        run_dashboard = self.run_dashboard
        keywords = self.keywords
        description = self.description
        google_map = self.google_map
        google_analytics = self.google_analytics
        add_this = self.add_this
        proxy_url_for_edit_mode = self.proxy_url_for_edit_mode
        embedded_dashboard = self.embedded_dashboard
        language_id = self.language_id
        identifier = self.identifier
        inode = self.inode
        force_execution = self.force_execution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if tag_storage is not UNSET:
            field_dict["tagStorage"] = tag_storage
        if site_thumbnail is not UNSET:
            field_dict["siteThumbnail"] = site_thumbnail
        if run_dashboard is not UNSET:
            field_dict["runDashboard"] = run_dashboard
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if description is not UNSET:
            field_dict["description"] = description
        if google_map is not UNSET:
            field_dict["googleMap"] = google_map
        if google_analytics is not UNSET:
            field_dict["googleAnalytics"] = google_analytics
        if add_this is not UNSET:
            field_dict["addThis"] = add_this
        if proxy_url_for_edit_mode is not UNSET:
            field_dict["proxyUrlForEditMode"] = proxy_url_for_edit_mode
        if embedded_dashboard is not UNSET:
            field_dict["embeddedDashboard"] = embedded_dashboard
        if language_id is not UNSET:
            field_dict["languageId"] = language_id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if inode is not UNSET:
            field_dict["inode"] = inode
        if force_execution is not UNSET:
            field_dict["forceExecution"] = force_execution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aliases = d.pop("aliases", UNSET)

        site_name = d.pop("siteName", UNSET)

        tag_storage = d.pop("tagStorage", UNSET)

        site_thumbnail = d.pop("siteThumbnail", UNSET)

        run_dashboard = d.pop("runDashboard", UNSET)

        keywords = d.pop("keywords", UNSET)

        description = d.pop("description", UNSET)

        google_map = d.pop("googleMap", UNSET)

        google_analytics = d.pop("googleAnalytics", UNSET)

        add_this = d.pop("addThis", UNSET)

        proxy_url_for_edit_mode = d.pop("proxyUrlForEditMode", UNSET)

        embedded_dashboard = d.pop("embeddedDashboard", UNSET)

        language_id = d.pop("languageId", UNSET)

        identifier = d.pop("identifier", UNSET)

        inode = d.pop("inode", UNSET)

        force_execution = d.pop("forceExecution", UNSET)

        site_form = cls(
            aliases=aliases,
            site_name=site_name,
            tag_storage=tag_storage,
            site_thumbnail=site_thumbnail,
            run_dashboard=run_dashboard,
            keywords=keywords,
            description=description,
            google_map=google_map,
            google_analytics=google_analytics,
            add_this=add_this,
            proxy_url_for_edit_mode=proxy_url_for_edit_mode,
            embedded_dashboard=embedded_dashboard,
            language_id=language_id,
            identifier=identifier,
            inode=inode,
            force_execution=force_execution,
        )

        site_form.additional_properties = d
        return site_form

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
