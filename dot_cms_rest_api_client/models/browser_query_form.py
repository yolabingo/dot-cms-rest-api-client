from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrowserQueryForm")


@attr.s(auto_attribs=True)
class BrowserQueryForm:
    """
    Attributes:
        host_folder_id (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        sort_by (Union[Unset, str]):
        offset (Union[Unset, int]):
        max_results (Union[Unset, int]):
        show_working (Union[Unset, bool]):
        show_archived (Union[Unset, bool]):
        show_folders (Union[Unset, bool]):
        show_files (Union[Unset, bool]):
        show_pages (Union[Unset, bool]):
        sort_by_desc (Union[Unset, bool]):
        show_links (Union[Unset, bool]):
        show_dot_assets (Union[Unset, bool]):
        language_id (Union[Unset, int]):
        extensions (Union[Unset, List[str]]):
        mime_types (Union[Unset, List[str]]):
    """

    host_folder_id: Union[Unset, str] = UNSET
    filter_: Union[Unset, str] = UNSET
    sort_by: Union[Unset, str] = UNSET
    offset: Union[Unset, int] = UNSET
    max_results: Union[Unset, int] = UNSET
    show_working: Union[Unset, bool] = UNSET
    show_archived: Union[Unset, bool] = UNSET
    show_folders: Union[Unset, bool] = UNSET
    show_files: Union[Unset, bool] = UNSET
    show_pages: Union[Unset, bool] = UNSET
    sort_by_desc: Union[Unset, bool] = UNSET
    show_links: Union[Unset, bool] = UNSET
    show_dot_assets: Union[Unset, bool] = UNSET
    language_id: Union[Unset, int] = UNSET
    extensions: Union[Unset, List[str]] = UNSET
    mime_types: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host_folder_id = self.host_folder_id
        filter_ = self.filter_
        sort_by = self.sort_by
        offset = self.offset
        max_results = self.max_results
        show_working = self.show_working
        show_archived = self.show_archived
        show_folders = self.show_folders
        show_files = self.show_files
        show_pages = self.show_pages
        sort_by_desc = self.sort_by_desc
        show_links = self.show_links
        show_dot_assets = self.show_dot_assets
        language_id = self.language_id
        extensions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions

        mime_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mime_types, Unset):
            mime_types = self.mime_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host_folder_id is not UNSET:
            field_dict["hostFolderId"] = host_folder_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if offset is not UNSET:
            field_dict["offset"] = offset
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if show_working is not UNSET:
            field_dict["showWorking"] = show_working
        if show_archived is not UNSET:
            field_dict["showArchived"] = show_archived
        if show_folders is not UNSET:
            field_dict["showFolders"] = show_folders
        if show_files is not UNSET:
            field_dict["showFiles"] = show_files
        if show_pages is not UNSET:
            field_dict["showPages"] = show_pages
        if sort_by_desc is not UNSET:
            field_dict["sortByDesc"] = sort_by_desc
        if show_links is not UNSET:
            field_dict["showLinks"] = show_links
        if show_dot_assets is not UNSET:
            field_dict["showDotAssets"] = show_dot_assets
        if language_id is not UNSET:
            field_dict["languageId"] = language_id
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if mime_types is not UNSET:
            field_dict["mimeTypes"] = mime_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host_folder_id = d.pop("hostFolderId", UNSET)

        filter_ = d.pop("filter", UNSET)

        sort_by = d.pop("sortBy", UNSET)

        offset = d.pop("offset", UNSET)

        max_results = d.pop("maxResults", UNSET)

        show_working = d.pop("showWorking", UNSET)

        show_archived = d.pop("showArchived", UNSET)

        show_folders = d.pop("showFolders", UNSET)

        show_files = d.pop("showFiles", UNSET)

        show_pages = d.pop("showPages", UNSET)

        sort_by_desc = d.pop("sortByDesc", UNSET)

        show_links = d.pop("showLinks", UNSET)

        show_dot_assets = d.pop("showDotAssets", UNSET)

        language_id = d.pop("languageId", UNSET)

        extensions = cast(List[str], d.pop("extensions", UNSET))

        mime_types = cast(List[str], d.pop("mimeTypes", UNSET))

        browser_query_form = cls(
            host_folder_id=host_folder_id,
            filter_=filter_,
            sort_by=sort_by,
            offset=offset,
            max_results=max_results,
            show_working=show_working,
            show_archived=show_archived,
            show_folders=show_folders,
            show_files=show_files,
            show_pages=show_pages,
            sort_by_desc=sort_by_desc,
            show_links=show_links,
            show_dot_assets=show_dot_assets,
            language_id=language_id,
            extensions=extensions,
            mime_types=mime_types,
        )

        browser_query_form.additional_properties = d
        return browser_query_form

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
