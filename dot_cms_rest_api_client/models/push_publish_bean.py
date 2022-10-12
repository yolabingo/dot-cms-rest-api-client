from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PushPublishBean")


@attr.s(auto_attribs=True)
class PushPublishBean:
    """
    Attributes:
        where_to_send (Union[Unset, str]):
        publish_date (Union[Unset, str]):
        publish_time (Union[Unset, str]):
        expire_date (Union[Unset, str]):
        expire_time (Union[Unset, str]):
        never_expire (Union[Unset, str]):
        filter_key (Union[Unset, str]):
        i_want_to (Union[Unset, str]):
        timezone_id (Union[Unset, str]):
        iwant_to (Union[Unset, str]):
    """

    where_to_send: Union[Unset, str] = UNSET
    publish_date: Union[Unset, str] = UNSET
    publish_time: Union[Unset, str] = UNSET
    expire_date: Union[Unset, str] = UNSET
    expire_time: Union[Unset, str] = UNSET
    never_expire: Union[Unset, str] = UNSET
    filter_key: Union[Unset, str] = UNSET
    i_want_to: Union[Unset, str] = UNSET
    timezone_id: Union[Unset, str] = UNSET
    iwant_to: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        where_to_send = self.where_to_send
        publish_date = self.publish_date
        publish_time = self.publish_time
        expire_date = self.expire_date
        expire_time = self.expire_time
        never_expire = self.never_expire
        filter_key = self.filter_key
        i_want_to = self.i_want_to
        timezone_id = self.timezone_id
        iwant_to = self.iwant_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if where_to_send is not UNSET:
            field_dict["whereToSend"] = where_to_send
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
        if filter_key is not UNSET:
            field_dict["filterKey"] = filter_key
        if i_want_to is not UNSET:
            field_dict["iWantTo"] = i_want_to
        if timezone_id is not UNSET:
            field_dict["timezoneId"] = timezone_id
        if iwant_to is not UNSET:
            field_dict["iwantTo"] = iwant_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        where_to_send = d.pop("whereToSend", UNSET)

        publish_date = d.pop("publishDate", UNSET)

        publish_time = d.pop("publishTime", UNSET)

        expire_date = d.pop("expireDate", UNSET)

        expire_time = d.pop("expireTime", UNSET)

        never_expire = d.pop("neverExpire", UNSET)

        filter_key = d.pop("filterKey", UNSET)

        i_want_to = d.pop("iWantTo", UNSET)

        timezone_id = d.pop("timezoneId", UNSET)

        iwant_to = d.pop("iwantTo", UNSET)

        push_publish_bean = cls(
            where_to_send=where_to_send,
            publish_date=publish_date,
            publish_time=publish_time,
            expire_date=expire_date,
            expire_time=expire_time,
            never_expire=never_expire,
            filter_key=filter_key,
            i_want_to=i_want_to,
            timezone_id=timezone_id,
            iwant_to=iwant_to,
        )

        push_publish_bean.additional_properties = d
        return push_publish_bean

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
