from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.fire_multiple_action_form_contentlet_item import FireMultipleActionFormContentletItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="FireMultipleActionForm")


@attr.s(auto_attribs=True)
class FireMultipleActionForm:
    """
    Attributes:
        comments (Union[Unset, str]):
        assign (Union[Unset, str]):
        publish_date (Union[Unset, str]):
        publish_time (Union[Unset, str]):
        expire_date (Union[Unset, str]):
        expire_time (Union[Unset, str]):
        never_expire (Union[Unset, str]):
        where_to_send (Union[Unset, str]):
        filter_key (Union[Unset, str]):
        timezone_id (Union[Unset, str]):
        iwant_to (Union[Unset, str]):
        contentlet (Union[Unset, List[FireMultipleActionFormContentletItem]]):
    """

    comments: Union[Unset, str] = UNSET
    assign: Union[Unset, str] = UNSET
    publish_date: Union[Unset, str] = UNSET
    publish_time: Union[Unset, str] = UNSET
    expire_date: Union[Unset, str] = UNSET
    expire_time: Union[Unset, str] = UNSET
    never_expire: Union[Unset, str] = UNSET
    where_to_send: Union[Unset, str] = UNSET
    filter_key: Union[Unset, str] = UNSET
    timezone_id: Union[Unset, str] = UNSET
    iwant_to: Union[Unset, str] = UNSET
    contentlet: Union[Unset, List[FireMultipleActionFormContentletItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comments = self.comments
        assign = self.assign
        publish_date = self.publish_date
        publish_time = self.publish_time
        expire_date = self.expire_date
        expire_time = self.expire_time
        never_expire = self.never_expire
        where_to_send = self.where_to_send
        filter_key = self.filter_key
        timezone_id = self.timezone_id
        iwant_to = self.iwant_to
        contentlet: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contentlet, Unset):
            contentlet = []
            for contentlet_item_data in self.contentlet:
                contentlet_item = contentlet_item_data.to_dict()

                contentlet.append(contentlet_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if assign is not UNSET:
            field_dict["assign"] = assign
        if publish_date is not UNSET:
            field_dict["publishDate"] = publish_date
        if publish_time is not UNSET:
            field_dict["publishTime"] = publish_time
        if expire_date is not UNSET:
            field_dict["expireDate"] = expire_date
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if never_expire is not UNSET:
            field_dict["neverExpire"] = never_expire
        if where_to_send is not UNSET:
            field_dict["whereToSend"] = where_to_send
        if filter_key is not UNSET:
            field_dict["filterKey"] = filter_key
        if timezone_id is not UNSET:
            field_dict["timezoneId"] = timezone_id
        if iwant_to is not UNSET:
            field_dict["iwantTo"] = iwant_to
        if contentlet is not UNSET:
            field_dict["contentlet"] = contentlet

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        comments = d.pop("comments", UNSET)

        assign = d.pop("assign", UNSET)

        publish_date = d.pop("publishDate", UNSET)

        publish_time = d.pop("publishTime", UNSET)

        expire_date = d.pop("expireDate", UNSET)

        expire_time = d.pop("expireTime", UNSET)

        never_expire = d.pop("neverExpire", UNSET)

        where_to_send = d.pop("whereToSend", UNSET)

        filter_key = d.pop("filterKey", UNSET)

        timezone_id = d.pop("timezoneId", UNSET)

        iwant_to = d.pop("iwantTo", UNSET)

        contentlet = []
        _contentlet = d.pop("contentlet", UNSET)
        for contentlet_item_data in _contentlet or []:
            contentlet_item = FireMultipleActionFormContentletItem.from_dict(contentlet_item_data)

            contentlet.append(contentlet_item)

        fire_multiple_action_form = cls(
            comments=comments,
            assign=assign,
            publish_date=publish_date,
            publish_time=publish_time,
            expire_date=expire_date,
            expire_time=expire_time,
            never_expire=never_expire,
            where_to_send=where_to_send,
            filter_key=filter_key,
            timezone_id=timezone_id,
            iwant_to=iwant_to,
            contentlet=contentlet,
        )

        fire_multiple_action_form.additional_properties = d
        return fire_multiple_action_form

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
