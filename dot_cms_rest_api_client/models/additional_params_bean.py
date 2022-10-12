from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.additional_params_bean_additional_params_map import AdditionalParamsBeanAdditionalParamsMap
from ..models.assign_comment_bean import AssignCommentBean
from ..models.push_publish_bean import PushPublishBean
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdditionalParamsBean")


@attr.s(auto_attribs=True)
class AdditionalParamsBean:
    """
    Attributes:
        push_publish (Union[Unset, PushPublishBean]):
        assign_comment (Union[Unset, AssignCommentBean]):
        additional_params_map (Union[Unset, AdditionalParamsBeanAdditionalParamsMap]):
        push_publish_bean (Union[Unset, PushPublishBean]):
        assign_comment_bean (Union[Unset, AssignCommentBean]):
    """

    push_publish: Union[Unset, PushPublishBean] = UNSET
    assign_comment: Union[Unset, AssignCommentBean] = UNSET
    additional_params_map: Union[Unset, AdditionalParamsBeanAdditionalParamsMap] = UNSET
    push_publish_bean: Union[Unset, PushPublishBean] = UNSET
    assign_comment_bean: Union[Unset, AssignCommentBean] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        push_publish: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.push_publish, Unset):
            push_publish = self.push_publish.to_dict()

        assign_comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assign_comment, Unset):
            assign_comment = self.assign_comment.to_dict()

        additional_params_map: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_params_map, Unset):
            additional_params_map = self.additional_params_map.to_dict()

        push_publish_bean: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.push_publish_bean, Unset):
            push_publish_bean = self.push_publish_bean.to_dict()

        assign_comment_bean: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assign_comment_bean, Unset):
            assign_comment_bean = self.assign_comment_bean.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if push_publish is not UNSET:
            field_dict["pushPublish"] = push_publish
        if assign_comment is not UNSET:
            field_dict["assignComment"] = assign_comment
        if additional_params_map is not UNSET:
            field_dict["additionalParamsMap"] = additional_params_map
        if push_publish_bean is not UNSET:
            field_dict["pushPublishBean"] = push_publish_bean
        if assign_comment_bean is not UNSET:
            field_dict["assignCommentBean"] = assign_comment_bean

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _push_publish = d.pop("pushPublish", UNSET)
        push_publish: Union[Unset, PushPublishBean]
        if isinstance(_push_publish, Unset):
            push_publish = UNSET
        else:
            push_publish = PushPublishBean.from_dict(_push_publish)

        _assign_comment = d.pop("assignComment", UNSET)
        assign_comment: Union[Unset, AssignCommentBean]
        if isinstance(_assign_comment, Unset):
            assign_comment = UNSET
        else:
            assign_comment = AssignCommentBean.from_dict(_assign_comment)

        _additional_params_map = d.pop("additionalParamsMap", UNSET)
        additional_params_map: Union[Unset, AdditionalParamsBeanAdditionalParamsMap]
        if isinstance(_additional_params_map, Unset):
            additional_params_map = UNSET
        else:
            additional_params_map = AdditionalParamsBeanAdditionalParamsMap.from_dict(_additional_params_map)

        _push_publish_bean = d.pop("pushPublishBean", UNSET)
        push_publish_bean: Union[Unset, PushPublishBean]
        if isinstance(_push_publish_bean, Unset):
            push_publish_bean = UNSET
        else:
            push_publish_bean = PushPublishBean.from_dict(_push_publish_bean)

        _assign_comment_bean = d.pop("assignCommentBean", UNSET)
        assign_comment_bean: Union[Unset, AssignCommentBean]
        if isinstance(_assign_comment_bean, Unset):
            assign_comment_bean = UNSET
        else:
            assign_comment_bean = AssignCommentBean.from_dict(_assign_comment_bean)

        additional_params_bean = cls(
            push_publish=push_publish,
            assign_comment=assign_comment,
            additional_params_map=additional_params_map,
            push_publish_bean=push_publish_bean,
            assign_comment_bean=assign_comment_bean,
        )

        additional_params_bean.additional_properties = d
        return additional_params_bean

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
