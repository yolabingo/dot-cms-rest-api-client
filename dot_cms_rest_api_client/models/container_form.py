from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.container_structure import ContainerStructure
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerForm")


@attr.s(auto_attribs=True)
class ContainerForm:
    """
    Attributes:
        identifier (Union[Unset, str]):
        title (Union[Unset, str]):
        friendly_name (Union[Unset, str]):
        max_contentlets (Union[Unset, int]):
        code (Union[Unset, str]):
        notes (Union[Unset, str]):
        pre_loop (Union[Unset, str]):
        post_loop (Union[Unset, str]):
        show_on_menu (Union[Unset, bool]):
        sort_order (Union[Unset, int]):
        sort_contentlets_by (Union[Unset, str]):
        structure_inode (Union[Unset, str]):
        container_structures (Union[Unset, List[ContainerStructure]]):
        owner (Union[Unset, str]):
        host_id (Union[Unset, str]):
        staticify (Union[Unset, bool]):
        use_div (Union[Unset, bool]):
        dynamic (Union[Unset, bool]):
    """

    identifier: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    max_contentlets: Union[Unset, int] = UNSET
    code: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    pre_loop: Union[Unset, str] = UNSET
    post_loop: Union[Unset, str] = UNSET
    show_on_menu: Union[Unset, bool] = UNSET
    sort_order: Union[Unset, int] = UNSET
    sort_contentlets_by: Union[Unset, str] = UNSET
    structure_inode: Union[Unset, str] = UNSET
    container_structures: Union[Unset, List[ContainerStructure]] = UNSET
    owner: Union[Unset, str] = UNSET
    host_id: Union[Unset, str] = UNSET
    staticify: Union[Unset, bool] = UNSET
    use_div: Union[Unset, bool] = UNSET
    dynamic: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        title = self.title
        friendly_name = self.friendly_name
        max_contentlets = self.max_contentlets
        code = self.code
        notes = self.notes
        pre_loop = self.pre_loop
        post_loop = self.post_loop
        show_on_menu = self.show_on_menu
        sort_order = self.sort_order
        sort_contentlets_by = self.sort_contentlets_by
        structure_inode = self.structure_inode
        container_structures: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.container_structures, Unset):
            container_structures = []
            for container_structures_item_data in self.container_structures:
                container_structures_item = container_structures_item_data.to_dict()

                container_structures.append(container_structures_item)

        owner = self.owner
        host_id = self.host_id
        staticify = self.staticify
        use_div = self.use_div
        dynamic = self.dynamic

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if title is not UNSET:
            field_dict["title"] = title
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if max_contentlets is not UNSET:
            field_dict["maxContentlets"] = max_contentlets
        if code is not UNSET:
            field_dict["code"] = code
        if notes is not UNSET:
            field_dict["notes"] = notes
        if pre_loop is not UNSET:
            field_dict["preLoop"] = pre_loop
        if post_loop is not UNSET:
            field_dict["postLoop"] = post_loop
        if show_on_menu is not UNSET:
            field_dict["showOnMenu"] = show_on_menu
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if sort_contentlets_by is not UNSET:
            field_dict["sortContentletsBy"] = sort_contentlets_by
        if structure_inode is not UNSET:
            field_dict["structureInode"] = structure_inode
        if container_structures is not UNSET:
            field_dict["containerStructures"] = container_structures
        if owner is not UNSET:
            field_dict["owner"] = owner
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if staticify is not UNSET:
            field_dict["staticify"] = staticify
        if use_div is not UNSET:
            field_dict["useDiv"] = use_div
        if dynamic is not UNSET:
            field_dict["dynamic"] = dynamic

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier", UNSET)

        title = d.pop("title", UNSET)

        friendly_name = d.pop("friendlyName", UNSET)

        max_contentlets = d.pop("maxContentlets", UNSET)

        code = d.pop("code", UNSET)

        notes = d.pop("notes", UNSET)

        pre_loop = d.pop("preLoop", UNSET)

        post_loop = d.pop("postLoop", UNSET)

        show_on_menu = d.pop("showOnMenu", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        sort_contentlets_by = d.pop("sortContentletsBy", UNSET)

        structure_inode = d.pop("structureInode", UNSET)

        container_structures = []
        _container_structures = d.pop("containerStructures", UNSET)
        for container_structures_item_data in _container_structures or []:
            container_structures_item = ContainerStructure.from_dict(container_structures_item_data)

            container_structures.append(container_structures_item)

        owner = d.pop("owner", UNSET)

        host_id = d.pop("hostId", UNSET)

        staticify = d.pop("staticify", UNSET)

        use_div = d.pop("useDiv", UNSET)

        dynamic = d.pop("dynamic", UNSET)

        container_form = cls(
            identifier=identifier,
            title=title,
            friendly_name=friendly_name,
            max_contentlets=max_contentlets,
            code=code,
            notes=notes,
            pre_loop=pre_loop,
            post_loop=post_loop,
            show_on_menu=show_on_menu,
            sort_order=sort_order,
            sort_contentlets_by=sort_contentlets_by,
            structure_inode=structure_inode,
            container_structures=container_structures,
            owner=owner,
            host_id=host_id,
            staticify=staticify,
            use_div=use_div,
            dynamic=dynamic,
        )

        container_form.additional_properties = d
        return container_form

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
