from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.content_type import ContentType
from ..models.content_type_form_iterable import ContentTypeFormIterable
from ..models.content_type_form_request_json import ContentTypeFormRequestJson
from ..models.tuple_2_system_action_string import Tuple2SystemActionString
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentTypeForm")


@attr.s(auto_attribs=True)
class ContentTypeForm:
    """
    Attributes:
        request_json (Union[Unset, ContentTypeFormRequestJson]):
        content_type (Union[Unset, ContentType]):
        iterable (Union[Unset, ContentTypeFormIterable]):
        system_actions (Union[Unset, List[Tuple2SystemActionString]]):
        workflows_ids (Union[Unset, List[str]]):
    """

    request_json: Union[Unset, ContentTypeFormRequestJson] = UNSET
    content_type: Union[Unset, ContentType] = UNSET
    iterable: Union[Unset, ContentTypeFormIterable] = UNSET
    system_actions: Union[Unset, List[Tuple2SystemActionString]] = UNSET
    workflows_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.request_json, Unset):
            request_json = self.request_json.to_dict()

        content_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.to_dict()

        iterable: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.iterable, Unset):
            iterable = self.iterable.to_dict()

        system_actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.system_actions, Unset):
            system_actions = []
            for system_actions_item_data in self.system_actions:
                system_actions_item = system_actions_item_data.to_dict()

                system_actions.append(system_actions_item)

        workflows_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.workflows_ids, Unset):
            workflows_ids = self.workflows_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_json is not UNSET:
            field_dict["requestJson"] = request_json
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if iterable is not UNSET:
            field_dict["iterable"] = iterable
        if system_actions is not UNSET:
            field_dict["systemActions"] = system_actions
        if workflows_ids is not UNSET:
            field_dict["workflowsIds"] = workflows_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _request_json = d.pop("requestJson", UNSET)
        request_json: Union[Unset, ContentTypeFormRequestJson]
        if isinstance(_request_json, Unset):
            request_json = UNSET
        else:
            request_json = ContentTypeFormRequestJson.from_dict(_request_json)

        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, ContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = ContentType.from_dict(_content_type)

        _iterable = d.pop("iterable", UNSET)
        iterable: Union[Unset, ContentTypeFormIterable]
        if isinstance(_iterable, Unset):
            iterable = UNSET
        else:
            iterable = ContentTypeFormIterable.from_dict(_iterable)

        system_actions = []
        _system_actions = d.pop("systemActions", UNSET)
        for system_actions_item_data in _system_actions or []:
            system_actions_item = Tuple2SystemActionString.from_dict(system_actions_item_data)

            system_actions.append(system_actions_item)

        workflows_ids = cast(List[str], d.pop("workflowsIds", UNSET))

        content_type_form = cls(
            request_json=request_json,
            content_type=content_type,
            iterable=iterable,
            system_actions=system_actions,
            workflows_ids=workflows_ids,
        )

        content_type_form.additional_properties = d
        return content_type_form

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
