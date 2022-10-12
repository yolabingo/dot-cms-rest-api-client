from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignCommentBean")


@attr.s(auto_attribs=True)
class AssignCommentBean:
    """
    Attributes:
        assign (Union[Unset, str]):
        comment (Union[Unset, str]):
    """

    assign: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assign = self.assign
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assign is not UNSET:
            field_dict["assign"] = assign
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assign = d.pop("assign", UNSET)

        comment = d.pop("comment", UNSET)

        assign_comment_bean = cls(
            assign=assign,
            comment=comment,
        )

        assign_comment_bean.additional_properties = d
        return assign_comment_bean

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
