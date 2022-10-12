import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.field import Field
from ..models.persona_index_policy_dependencies import PersonaIndexPolicyDependencies
from ..models.persona_map import PersonaMap
from ..models.user_api import UserAPI
from ..types import UNSET, Unset

T = TypeVar("T", bound="Persona")


@attr.s(auto_attribs=True)
class Persona:
    """
    Attributes:
        map_ (Union[Unset, PersonaMap]):
        low_index_priority (Union[Unset, bool]):
        user_api (Union[Unset, UserAPI]):
        index_policy_dependencies (Union[Unset, PersonaIndexPolicyDependencies]):
        description (Union[Unset, str]):
        tags (Union[Unset, str]):
        key_tag (Union[Unset, str]):
        name (Union[Unset, str]):
        identifier (Union[Unset, str]):
        inode (Union[Unset, str]):
        live (Union[Unset, bool]):
        title (Union[Unset, str]):
        working (Union[Unset, bool]):
        archived (Union[Unset, bool]):
        version_type (Union[Unset, str]):
        mod_date (Union[Unset, datetime.datetime]):
        version_id (Union[Unset, str]):
        mod_user (Union[Unset, str]):
        locked (Union[Unset, bool]):
        owner (Union[Unset, str]):
        permission_id (Union[Unset, str]):
        permission_type (Union[Unset, str]):
        host (Union[Unset, str]):
        new (Union[Unset, bool]):
        language_id (Union[Unset, int]):
        folder (Union[Unset, str]):
        file_asset (Union[Unset, bool]):
        structure_inode (Union[Unset, str]):
        system_host (Union[Unset, bool]):
        category_id (Union[Unset, str]):
        content_type_id (Union[Unset, str]):
        sort_order (Union[Unset, int]):
        title_image (Union[Unset, Field]):
        htmlpage (Union[Unset, bool]):
        dot_asset (Union[Unset, bool]):
        persona (Union[Unset, bool]):
        form (Union[Unset, bool]):
        vanity_url (Union[Unset, bool]):
        key_value (Union[Unset, bool]):
        type (Union[Unset, str]):
    """

    map_: Union[Unset, PersonaMap] = UNSET
    low_index_priority: Union[Unset, bool] = UNSET
    user_api: Union[Unset, UserAPI] = UNSET
    index_policy_dependencies: Union[Unset, PersonaIndexPolicyDependencies] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, str] = UNSET
    key_tag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    identifier: Union[Unset, str] = UNSET
    inode: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    working: Union[Unset, bool] = UNSET
    archived: Union[Unset, bool] = UNSET
    version_type: Union[Unset, str] = UNSET
    mod_date: Union[Unset, datetime.datetime] = UNSET
    version_id: Union[Unset, str] = UNSET
    mod_user: Union[Unset, str] = UNSET
    locked: Union[Unset, bool] = UNSET
    owner: Union[Unset, str] = UNSET
    permission_id: Union[Unset, str] = UNSET
    permission_type: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    new: Union[Unset, bool] = UNSET
    language_id: Union[Unset, int] = UNSET
    folder: Union[Unset, str] = UNSET
    file_asset: Union[Unset, bool] = UNSET
    structure_inode: Union[Unset, str] = UNSET
    system_host: Union[Unset, bool] = UNSET
    category_id: Union[Unset, str] = UNSET
    content_type_id: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET
    title_image: Union[Unset, Field] = UNSET
    htmlpage: Union[Unset, bool] = UNSET
    dot_asset: Union[Unset, bool] = UNSET
    persona: Union[Unset, bool] = UNSET
    form: Union[Unset, bool] = UNSET
    vanity_url: Union[Unset, bool] = UNSET
    key_value: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        map_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_, Unset):
            map_ = self.map_.to_dict()

        low_index_priority = self.low_index_priority
        user_api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_api, Unset):
            user_api = self.user_api.to_dict()

        index_policy_dependencies: Union[Unset, str] = UNSET
        if not isinstance(self.index_policy_dependencies, Unset):
            index_policy_dependencies = self.index_policy_dependencies.value

        description = self.description
        tags = self.tags
        key_tag = self.key_tag
        name = self.name
        identifier = self.identifier
        inode = self.inode
        live = self.live
        title = self.title
        working = self.working
        archived = self.archived
        version_type = self.version_type
        mod_date: Union[Unset, str] = UNSET
        if not isinstance(self.mod_date, Unset):
            mod_date = self.mod_date.isoformat()

        version_id = self.version_id
        mod_user = self.mod_user
        locked = self.locked
        owner = self.owner
        permission_id = self.permission_id
        permission_type = self.permission_type
        host = self.host
        new = self.new
        language_id = self.language_id
        folder = self.folder
        file_asset = self.file_asset
        structure_inode = self.structure_inode
        system_host = self.system_host
        category_id = self.category_id
        content_type_id = self.content_type_id
        sort_order = self.sort_order
        title_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.title_image, Unset):
            title_image = self.title_image.to_dict()

        htmlpage = self.htmlpage
        dot_asset = self.dot_asset
        persona = self.persona
        form = self.form
        vanity_url = self.vanity_url
        key_value = self.key_value
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if map_ is not UNSET:
            field_dict["map"] = map_
        if low_index_priority is not UNSET:
            field_dict["lowIndexPriority"] = low_index_priority
        if user_api is not UNSET:
            field_dict["userAPI"] = user_api
        if index_policy_dependencies is not UNSET:
            field_dict["indexPolicyDependencies"] = index_policy_dependencies
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if key_tag is not UNSET:
            field_dict["keyTag"] = key_tag
        if name is not UNSET:
            field_dict["name"] = name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if inode is not UNSET:
            field_dict["inode"] = inode
        if live is not UNSET:
            field_dict["live"] = live
        if title is not UNSET:
            field_dict["title"] = title
        if working is not UNSET:
            field_dict["working"] = working
        if archived is not UNSET:
            field_dict["archived"] = archived
        if version_type is not UNSET:
            field_dict["versionType"] = version_type
        if mod_date is not UNSET:
            field_dict["modDate"] = mod_date
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if mod_user is not UNSET:
            field_dict["modUser"] = mod_user
        if locked is not UNSET:
            field_dict["locked"] = locked
        if owner is not UNSET:
            field_dict["owner"] = owner
        if permission_id is not UNSET:
            field_dict["permissionId"] = permission_id
        if permission_type is not UNSET:
            field_dict["permissionType"] = permission_type
        if host is not UNSET:
            field_dict["host"] = host
        if new is not UNSET:
            field_dict["new"] = new
        if language_id is not UNSET:
            field_dict["languageId"] = language_id
        if folder is not UNSET:
            field_dict["folder"] = folder
        if file_asset is not UNSET:
            field_dict["fileAsset"] = file_asset
        if structure_inode is not UNSET:
            field_dict["structureInode"] = structure_inode
        if system_host is not UNSET:
            field_dict["systemHost"] = system_host
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if content_type_id is not UNSET:
            field_dict["contentTypeId"] = content_type_id
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if title_image is not UNSET:
            field_dict["titleImage"] = title_image
        if htmlpage is not UNSET:
            field_dict["htmlpage"] = htmlpage
        if dot_asset is not UNSET:
            field_dict["dotAsset"] = dot_asset
        if persona is not UNSET:
            field_dict["persona"] = persona
        if form is not UNSET:
            field_dict["form"] = form
        if vanity_url is not UNSET:
            field_dict["vanityUrl"] = vanity_url
        if key_value is not UNSET:
            field_dict["keyValue"] = key_value
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _map_ = d.pop("map", UNSET)
        map_: Union[Unset, PersonaMap]
        if isinstance(_map_, Unset):
            map_ = UNSET
        else:
            map_ = PersonaMap.from_dict(_map_)

        low_index_priority = d.pop("lowIndexPriority", UNSET)

        _user_api = d.pop("userAPI", UNSET)
        user_api: Union[Unset, UserAPI]
        if isinstance(_user_api, Unset):
            user_api = UNSET
        else:
            user_api = UserAPI.from_dict(_user_api)

        _index_policy_dependencies = d.pop("indexPolicyDependencies", UNSET)
        index_policy_dependencies: Union[Unset, PersonaIndexPolicyDependencies]
        if isinstance(_index_policy_dependencies, Unset):
            index_policy_dependencies = UNSET
        else:
            index_policy_dependencies = PersonaIndexPolicyDependencies(_index_policy_dependencies)

        description = d.pop("description", UNSET)

        tags = d.pop("tags", UNSET)

        key_tag = d.pop("keyTag", UNSET)

        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        inode = d.pop("inode", UNSET)

        live = d.pop("live", UNSET)

        title = d.pop("title", UNSET)

        working = d.pop("working", UNSET)

        archived = d.pop("archived", UNSET)

        version_type = d.pop("versionType", UNSET)

        _mod_date = d.pop("modDate", UNSET)
        mod_date: Union[Unset, datetime.datetime]
        if isinstance(_mod_date, Unset):
            mod_date = UNSET
        else:
            mod_date = isoparse(_mod_date)

        version_id = d.pop("versionId", UNSET)

        mod_user = d.pop("modUser", UNSET)

        locked = d.pop("locked", UNSET)

        owner = d.pop("owner", UNSET)

        permission_id = d.pop("permissionId", UNSET)

        permission_type = d.pop("permissionType", UNSET)

        host = d.pop("host", UNSET)

        new = d.pop("new", UNSET)

        language_id = d.pop("languageId", UNSET)

        folder = d.pop("folder", UNSET)

        file_asset = d.pop("fileAsset", UNSET)

        structure_inode = d.pop("structureInode", UNSET)

        system_host = d.pop("systemHost", UNSET)

        category_id = d.pop("categoryId", UNSET)

        content_type_id = d.pop("contentTypeId", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        _title_image = d.pop("titleImage", UNSET)
        title_image: Union[Unset, Field]
        if isinstance(_title_image, Unset):
            title_image = UNSET
        else:
            title_image = Field.from_dict(_title_image)

        htmlpage = d.pop("htmlpage", UNSET)

        dot_asset = d.pop("dotAsset", UNSET)

        persona = d.pop("persona", UNSET)

        form = d.pop("form", UNSET)

        vanity_url = d.pop("vanityUrl", UNSET)

        key_value = d.pop("keyValue", UNSET)

        type = d.pop("type", UNSET)

        persona = cls(
            map_=map_,
            low_index_priority=low_index_priority,
            user_api=user_api,
            index_policy_dependencies=index_policy_dependencies,
            description=description,
            tags=tags,
            key_tag=key_tag,
            name=name,
            identifier=identifier,
            inode=inode,
            live=live,
            title=title,
            working=working,
            archived=archived,
            version_type=version_type,
            mod_date=mod_date,
            version_id=version_id,
            mod_user=mod_user,
            locked=locked,
            owner=owner,
            permission_id=permission_id,
            permission_type=permission_type,
            host=host,
            new=new,
            language_id=language_id,
            folder=folder,
            file_asset=file_asset,
            structure_inode=structure_inode,
            system_host=system_host,
            category_id=category_id,
            content_type_id=content_type_id,
            sort_order=sort_order,
            title_image=title_image,
            htmlpage=htmlpage,
            dot_asset=dot_asset,
            persona=persona,
            form=form,
            vanity_url=vanity_url,
            key_value=key_value,
            type=type,
        )

        persona.additional_properties = d
        return persona

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
