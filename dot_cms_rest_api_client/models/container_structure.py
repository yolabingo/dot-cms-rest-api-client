from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerStructure")


@attr.s(auto_attribs=True)
class ContainerStructure:
    """
    Attributes:
        id (Union[Unset, str]):
        structure_id (Union[Unset, str]):
        container_inode (Union[Unset, str]):
        container_id (Union[Unset, str]):
        code (Union[Unset, str]):
        content_type_var (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    structure_id: Union[Unset, str] = UNSET
    container_inode: Union[Unset, str] = UNSET
    container_id: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    content_type_var: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        structure_id = self.structure_id
        container_inode = self.container_inode
        container_id = self.container_id
        code = self.code
        content_type_var = self.content_type_var

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if structure_id is not UNSET:
            field_dict["structureId"] = structure_id
        if container_inode is not UNSET:
            field_dict["containerInode"] = container_inode
        if container_id is not UNSET:
            field_dict["containerId"] = container_id
        if code is not UNSET:
            field_dict["code"] = code
        if content_type_var is not UNSET:
            field_dict["contentTypeVar"] = content_type_var

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        structure_id = d.pop("structureId", UNSET)

        container_inode = d.pop("containerInode", UNSET)

        container_id = d.pop("containerId", UNSET)

        code = d.pop("code", UNSET)

        content_type_var = d.pop("contentTypeVar", UNSET)

        container_structure = cls(
            id=id,
            structure_id=structure_id,
            container_inode=container_inode,
            container_id=container_id,
            code=code,
            content_type_var=content_type_var,
        )

        container_structure.additional_properties = d
        return container_structure

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
