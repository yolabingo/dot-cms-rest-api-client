import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowScheme")


@attr.s(auto_attribs=True)
class WorkflowScheme:
    """
    Attributes:
        id (Union[Unset, str]):
        creation_date (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        archived (Union[Unset, bool]):
        mandatory (Union[Unset, bool]):
        default_scheme (Union[Unset, bool]):
        mod_date (Union[Unset, datetime.datetime]):
        entry_action_id (Union[Unset, str]):
        system (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    mandatory: Union[Unset, bool] = UNSET
    default_scheme: Union[Unset, bool] = UNSET
    mod_date: Union[Unset, datetime.datetime] = UNSET
    entry_action_id: Union[Unset, str] = UNSET
    system: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        name = self.name
        description = self.description
        archived = self.archived
        mandatory = self.mandatory
        default_scheme = self.default_scheme
        mod_date: Union[Unset, str] = UNSET
        if not isinstance(self.mod_date, Unset):
            mod_date = self.mod_date.isoformat()

        entry_action_id = self.entry_action_id
        system = self.system

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if archived is not UNSET:
            field_dict["archived"] = archived
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if default_scheme is not UNSET:
            field_dict["defaultScheme"] = default_scheme
        if mod_date is not UNSET:
            field_dict["modDate"] = mod_date
        if entry_action_id is not UNSET:
            field_dict["entryActionId"] = entry_action_id
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        archived = d.pop("archived", UNSET)

        mandatory = d.pop("mandatory", UNSET)

        default_scheme = d.pop("defaultScheme", UNSET)

        _mod_date = d.pop("modDate", UNSET)
        mod_date: Union[Unset, datetime.datetime]
        if isinstance(_mod_date, Unset):
            mod_date = UNSET
        else:
            mod_date = isoparse(_mod_date)

        entry_action_id = d.pop("entryActionId", UNSET)

        system = d.pop("system", UNSET)

        workflow_scheme = cls(
            id=id,
            creation_date=creation_date,
            name=name,
            description=description,
            archived=archived,
            mandatory=mandatory,
            default_scheme=default_scheme,
            mod_date=mod_date,
            entry_action_id=entry_action_id,
            system=system,
        )

        workflow_scheme.additional_properties = d
        return workflow_scheme

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
