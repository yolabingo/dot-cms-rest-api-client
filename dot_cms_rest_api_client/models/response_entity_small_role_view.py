from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.error_entity import ErrorEntity
from ..models.message_entity import MessageEntity
from ..models.response_entity_small_role_view_i18n_messages_map import ResponseEntitySmallRoleViewI18NMessagesMap
from ..models.small_role_view import SmallRoleView
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseEntitySmallRoleView")


@attr.s(auto_attribs=True)
class ResponseEntitySmallRoleView:
    """
    Attributes:
        errors (Union[Unset, List[ErrorEntity]]):
        entity (Union[Unset, List[SmallRoleView]]):
        messages (Union[Unset, List[MessageEntity]]):
        i_18_n_messages_map (Union[Unset, ResponseEntitySmallRoleViewI18NMessagesMap]):
        permissions (Union[Unset, List[str]]):
    """

    errors: Union[Unset, List[ErrorEntity]] = UNSET
    entity: Union[Unset, List[SmallRoleView]] = UNSET
    messages: Union[Unset, List[MessageEntity]] = UNSET
    i_18_n_messages_map: Union[Unset, ResponseEntitySmallRoleViewI18NMessagesMap] = UNSET
    permissions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        entity: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = []
            for entity_item_data in self.entity:
                entity_item = entity_item_data.to_dict()

                entity.append(entity_item)

        messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        i_18_n_messages_map: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.i_18_n_messages_map, Unset):
            i_18_n_messages_map = self.i_18_n_messages_map.to_dict()

        permissions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if entity is not UNSET:
            field_dict["entity"] = entity
        if messages is not UNSET:
            field_dict["messages"] = messages
        if i_18_n_messages_map is not UNSET:
            field_dict["i18nMessagesMap"] = i_18_n_messages_map
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ErrorEntity.from_dict(errors_item_data)

            errors.append(errors_item)

        entity = []
        _entity = d.pop("entity", UNSET)
        for entity_item_data in _entity or []:
            entity_item = SmallRoleView.from_dict(entity_item_data)

            entity.append(entity_item)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = MessageEntity.from_dict(messages_item_data)

            messages.append(messages_item)

        _i_18_n_messages_map = d.pop("i18nMessagesMap", UNSET)
        i_18_n_messages_map: Union[Unset, ResponseEntitySmallRoleViewI18NMessagesMap]
        if isinstance(_i_18_n_messages_map, Unset):
            i_18_n_messages_map = UNSET
        else:
            i_18_n_messages_map = ResponseEntitySmallRoleViewI18NMessagesMap.from_dict(_i_18_n_messages_map)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        response_entity_small_role_view = cls(
            errors=errors,
            entity=entity,
            messages=messages,
            i_18_n_messages_map=i_18_n_messages_map,
            permissions=permissions,
        )

        response_entity_small_role_view.additional_properties = d
        return response_entity_small_role_view

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
