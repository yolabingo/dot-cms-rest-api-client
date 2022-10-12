import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.role import Role
from ..models.user_additional_info import UserAdditionalInfo
from ..models.user_locale import UserLocale
from ..models.user_time_zone import UserTimeZone
from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        modification_date (Union[Unset, datetime.datetime]):
        locale (Union[Unset, UserLocale]):
        time_zone (Union[Unset, UserTimeZone]):
        full_name (Union[Unset, str]):
        default_user (Union[Unset, bool]):
        company_id (Union[Unset, str]):
        actual_company_id (Union[Unset, str]):
        password_expired (Union[Unset, bool]):
        female (Union[Unset, bool]):
        language_id (Union[Unset, str]):
        time_zone_id (Union[Unset, str]):
        resolution (Union[Unset, str]):
        refresh_rate (Union[Unset, str]):
        recipient_id (Union[Unset, str]):
        recipient_name (Union[Unset, str]):
        recipient_address (Union[Unset, str]):
        recipient_internet_address (Union[Unset, str]):
        multiple_recipients (Union[Unset, bool]):
        anonymous_user (Union[Unset, bool]):
        user_role (Union[Unset, Role]):
        password (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        email_address (Union[Unset, str]):
        user_id (Union[Unset, str]):
        additional_info (Union[Unset, UserAdditionalInfo]):
        password_expiration_date (Union[Unset, datetime.datetime]):
        middle_name (Union[Unset, str]):
        male (Union[Unset, bool]):
        skin_id (Union[Unset, str]):
        create_date (Union[Unset, datetime.datetime]):
        login_date (Union[Unset, datetime.datetime]):
        login_ip (Union[Unset, str]):
        last_login_date (Union[Unset, datetime.datetime]):
        last_login_ip (Union[Unset, str]):
        failed_login_attempts (Union[Unset, int]):
        agreed_to_terms_of_use (Union[Unset, bool]):
        active (Union[Unset, bool]):
        birthday (Union[Unset, datetime.datetime]):
        comments (Union[Unset, str]):
        nick_name (Union[Unset, str]):
        delete_in_progress (Union[Unset, bool]):
        delete_date (Union[Unset, datetime.datetime]):
        password_reset (Union[Unset, bool]):
        password_encrypted (Union[Unset, bool]):
        sms_id (Union[Unset, str]):
        aim_id (Union[Unset, str]):
        icq_id (Union[Unset, str]):
        msn_id (Union[Unset, str]):
        ym_id (Union[Unset, str]):
        favorite_activity (Union[Unset, str]):
        favorite_bible_verse (Union[Unset, str]):
        favorite_food (Union[Unset, str]):
        favorite_movie (Union[Unset, str]):
        favorite_music (Union[Unset, str]):
        dotted_skins (Union[Unset, bool]):
        rounded_skins (Union[Unset, bool]):
        greeting (Union[Unset, str]):
        layout_ids (Union[Unset, str]):
        new (Union[Unset, bool]):
        modified (Union[Unset, bool]):
    """

    modification_date: Union[Unset, datetime.datetime] = UNSET
    locale: Union[Unset, UserLocale] = UNSET
    time_zone: Union[Unset, UserTimeZone] = UNSET
    full_name: Union[Unset, str] = UNSET
    default_user: Union[Unset, bool] = UNSET
    company_id: Union[Unset, str] = UNSET
    actual_company_id: Union[Unset, str] = UNSET
    password_expired: Union[Unset, bool] = UNSET
    female: Union[Unset, bool] = UNSET
    language_id: Union[Unset, str] = UNSET
    time_zone_id: Union[Unset, str] = UNSET
    resolution: Union[Unset, str] = UNSET
    refresh_rate: Union[Unset, str] = UNSET
    recipient_id: Union[Unset, str] = UNSET
    recipient_name: Union[Unset, str] = UNSET
    recipient_address: Union[Unset, str] = UNSET
    recipient_internet_address: Union[Unset, str] = UNSET
    multiple_recipients: Union[Unset, bool] = UNSET
    anonymous_user: Union[Unset, bool] = UNSET
    user_role: Union[Unset, Role] = UNSET
    password: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_info: Union[Unset, UserAdditionalInfo] = UNSET
    password_expiration_date: Union[Unset, datetime.datetime] = UNSET
    middle_name: Union[Unset, str] = UNSET
    male: Union[Unset, bool] = UNSET
    skin_id: Union[Unset, str] = UNSET
    create_date: Union[Unset, datetime.datetime] = UNSET
    login_date: Union[Unset, datetime.datetime] = UNSET
    login_ip: Union[Unset, str] = UNSET
    last_login_date: Union[Unset, datetime.datetime] = UNSET
    last_login_ip: Union[Unset, str] = UNSET
    failed_login_attempts: Union[Unset, int] = UNSET
    agreed_to_terms_of_use: Union[Unset, bool] = UNSET
    active: Union[Unset, bool] = UNSET
    birthday: Union[Unset, datetime.datetime] = UNSET
    comments: Union[Unset, str] = UNSET
    nick_name: Union[Unset, str] = UNSET
    delete_in_progress: Union[Unset, bool] = UNSET
    delete_date: Union[Unset, datetime.datetime] = UNSET
    password_reset: Union[Unset, bool] = UNSET
    password_encrypted: Union[Unset, bool] = UNSET
    sms_id: Union[Unset, str] = UNSET
    aim_id: Union[Unset, str] = UNSET
    icq_id: Union[Unset, str] = UNSET
    msn_id: Union[Unset, str] = UNSET
    ym_id: Union[Unset, str] = UNSET
    favorite_activity: Union[Unset, str] = UNSET
    favorite_bible_verse: Union[Unset, str] = UNSET
    favorite_food: Union[Unset, str] = UNSET
    favorite_movie: Union[Unset, str] = UNSET
    favorite_music: Union[Unset, str] = UNSET
    dotted_skins: Union[Unset, bool] = UNSET
    rounded_skins: Union[Unset, bool] = UNSET
    greeting: Union[Unset, str] = UNSET
    layout_ids: Union[Unset, str] = UNSET
    new: Union[Unset, bool] = UNSET
    modified: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        modification_date: Union[Unset, str] = UNSET
        if not isinstance(self.modification_date, Unset):
            modification_date = self.modification_date.isoformat()

        locale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.to_dict()

        time_zone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_zone, Unset):
            time_zone = self.time_zone.to_dict()

        full_name = self.full_name
        default_user = self.default_user
        company_id = self.company_id
        actual_company_id = self.actual_company_id
        password_expired = self.password_expired
        female = self.female
        language_id = self.language_id
        time_zone_id = self.time_zone_id
        resolution = self.resolution
        refresh_rate = self.refresh_rate
        recipient_id = self.recipient_id
        recipient_name = self.recipient_name
        recipient_address = self.recipient_address
        recipient_internet_address = self.recipient_internet_address
        multiple_recipients = self.multiple_recipients
        anonymous_user = self.anonymous_user
        user_role: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_role, Unset):
            user_role = self.user_role.to_dict()

        password = self.password
        first_name = self.first_name
        last_name = self.last_name
        email_address = self.email_address
        user_id = self.user_id
        additional_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_info, Unset):
            additional_info = self.additional_info.to_dict()

        password_expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.password_expiration_date, Unset):
            password_expiration_date = self.password_expiration_date.isoformat()

        middle_name = self.middle_name
        male = self.male
        skin_id = self.skin_id
        create_date: Union[Unset, str] = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        login_date: Union[Unset, str] = UNSET
        if not isinstance(self.login_date, Unset):
            login_date = self.login_date.isoformat()

        login_ip = self.login_ip
        last_login_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_login_date, Unset):
            last_login_date = self.last_login_date.isoformat()

        last_login_ip = self.last_login_ip
        failed_login_attempts = self.failed_login_attempts
        agreed_to_terms_of_use = self.agreed_to_terms_of_use
        active = self.active
        birthday: Union[Unset, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        comments = self.comments
        nick_name = self.nick_name
        delete_in_progress = self.delete_in_progress
        delete_date: Union[Unset, str] = UNSET
        if not isinstance(self.delete_date, Unset):
            delete_date = self.delete_date.isoformat()

        password_reset = self.password_reset
        password_encrypted = self.password_encrypted
        sms_id = self.sms_id
        aim_id = self.aim_id
        icq_id = self.icq_id
        msn_id = self.msn_id
        ym_id = self.ym_id
        favorite_activity = self.favorite_activity
        favorite_bible_verse = self.favorite_bible_verse
        favorite_food = self.favorite_food
        favorite_movie = self.favorite_movie
        favorite_music = self.favorite_music
        dotted_skins = self.dotted_skins
        rounded_skins = self.rounded_skins
        greeting = self.greeting
        layout_ids = self.layout_ids
        new = self.new
        modified = self.modified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modification_date is not UNSET:
            field_dict["modificationDate"] = modification_date
        if locale is not UNSET:
            field_dict["locale"] = locale
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if default_user is not UNSET:
            field_dict["defaultUser"] = default_user
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if actual_company_id is not UNSET:
            field_dict["actualCompanyId"] = actual_company_id
        if password_expired is not UNSET:
            field_dict["passwordExpired"] = password_expired
        if female is not UNSET:
            field_dict["female"] = female
        if language_id is not UNSET:
            field_dict["languageId"] = language_id
        if time_zone_id is not UNSET:
            field_dict["timeZoneId"] = time_zone_id
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if refresh_rate is not UNSET:
            field_dict["refreshRate"] = refresh_rate
        if recipient_id is not UNSET:
            field_dict["recipientId"] = recipient_id
        if recipient_name is not UNSET:
            field_dict["recipientName"] = recipient_name
        if recipient_address is not UNSET:
            field_dict["recipientAddress"] = recipient_address
        if recipient_internet_address is not UNSET:
            field_dict["recipientInternetAddress"] = recipient_internet_address
        if multiple_recipients is not UNSET:
            field_dict["multipleRecipients"] = multiple_recipients
        if anonymous_user is not UNSET:
            field_dict["anonymousUser"] = anonymous_user
        if user_role is not UNSET:
            field_dict["userRole"] = user_role
        if password is not UNSET:
            field_dict["password"] = password
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if additional_info is not UNSET:
            field_dict["additionalInfo"] = additional_info
        if password_expiration_date is not UNSET:
            field_dict["passwordExpirationDate"] = password_expiration_date
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if male is not UNSET:
            field_dict["male"] = male
        if skin_id is not UNSET:
            field_dict["skinId"] = skin_id
        if create_date is not UNSET:
            field_dict["createDate"] = create_date
        if login_date is not UNSET:
            field_dict["loginDate"] = login_date
        if login_ip is not UNSET:
            field_dict["loginIP"] = login_ip
        if last_login_date is not UNSET:
            field_dict["lastLoginDate"] = last_login_date
        if last_login_ip is not UNSET:
            field_dict["lastLoginIP"] = last_login_ip
        if failed_login_attempts is not UNSET:
            field_dict["failedLoginAttempts"] = failed_login_attempts
        if agreed_to_terms_of_use is not UNSET:
            field_dict["agreedToTermsOfUse"] = agreed_to_terms_of_use
        if active is not UNSET:
            field_dict["active"] = active
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if comments is not UNSET:
            field_dict["comments"] = comments
        if nick_name is not UNSET:
            field_dict["nickName"] = nick_name
        if delete_in_progress is not UNSET:
            field_dict["deleteInProgress"] = delete_in_progress
        if delete_date is not UNSET:
            field_dict["deleteDate"] = delete_date
        if password_reset is not UNSET:
            field_dict["passwordReset"] = password_reset
        if password_encrypted is not UNSET:
            field_dict["passwordEncrypted"] = password_encrypted
        if sms_id is not UNSET:
            field_dict["smsId"] = sms_id
        if aim_id is not UNSET:
            field_dict["aimId"] = aim_id
        if icq_id is not UNSET:
            field_dict["icqId"] = icq_id
        if msn_id is not UNSET:
            field_dict["msnId"] = msn_id
        if ym_id is not UNSET:
            field_dict["ymId"] = ym_id
        if favorite_activity is not UNSET:
            field_dict["favoriteActivity"] = favorite_activity
        if favorite_bible_verse is not UNSET:
            field_dict["favoriteBibleVerse"] = favorite_bible_verse
        if favorite_food is not UNSET:
            field_dict["favoriteFood"] = favorite_food
        if favorite_movie is not UNSET:
            field_dict["favoriteMovie"] = favorite_movie
        if favorite_music is not UNSET:
            field_dict["favoriteMusic"] = favorite_music
        if dotted_skins is not UNSET:
            field_dict["dottedSkins"] = dotted_skins
        if rounded_skins is not UNSET:
            field_dict["roundedSkins"] = rounded_skins
        if greeting is not UNSET:
            field_dict["greeting"] = greeting
        if layout_ids is not UNSET:
            field_dict["layoutIds"] = layout_ids
        if new is not UNSET:
            field_dict["new"] = new
        if modified is not UNSET:
            field_dict["modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _modification_date = d.pop("modificationDate", UNSET)
        modification_date: Union[Unset, datetime.datetime]
        if isinstance(_modification_date, Unset):
            modification_date = UNSET
        else:
            modification_date = isoparse(_modification_date)

        _locale = d.pop("locale", UNSET)
        locale: Union[Unset, UserLocale]
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = UserLocale.from_dict(_locale)

        _time_zone = d.pop("timeZone", UNSET)
        time_zone: Union[Unset, UserTimeZone]
        if isinstance(_time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = UserTimeZone.from_dict(_time_zone)

        full_name = d.pop("fullName", UNSET)

        default_user = d.pop("defaultUser", UNSET)

        company_id = d.pop("companyId", UNSET)

        actual_company_id = d.pop("actualCompanyId", UNSET)

        password_expired = d.pop("passwordExpired", UNSET)

        female = d.pop("female", UNSET)

        language_id = d.pop("languageId", UNSET)

        time_zone_id = d.pop("timeZoneId", UNSET)

        resolution = d.pop("resolution", UNSET)

        refresh_rate = d.pop("refreshRate", UNSET)

        recipient_id = d.pop("recipientId", UNSET)

        recipient_name = d.pop("recipientName", UNSET)

        recipient_address = d.pop("recipientAddress", UNSET)

        recipient_internet_address = d.pop("recipientInternetAddress", UNSET)

        multiple_recipients = d.pop("multipleRecipients", UNSET)

        anonymous_user = d.pop("anonymousUser", UNSET)

        _user_role = d.pop("userRole", UNSET)
        user_role: Union[Unset, Role]
        if isinstance(_user_role, Unset):
            user_role = UNSET
        else:
            user_role = Role.from_dict(_user_role)

        password = d.pop("password", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        user_id = d.pop("userId", UNSET)

        _additional_info = d.pop("additionalInfo", UNSET)
        additional_info: Union[Unset, UserAdditionalInfo]
        if isinstance(_additional_info, Unset):
            additional_info = UNSET
        else:
            additional_info = UserAdditionalInfo.from_dict(_additional_info)

        _password_expiration_date = d.pop("passwordExpirationDate", UNSET)
        password_expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_password_expiration_date, Unset):
            password_expiration_date = UNSET
        else:
            password_expiration_date = isoparse(_password_expiration_date)

        middle_name = d.pop("middleName", UNSET)

        male = d.pop("male", UNSET)

        skin_id = d.pop("skinId", UNSET)

        _create_date = d.pop("createDate", UNSET)
        create_date: Union[Unset, datetime.datetime]
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        _login_date = d.pop("loginDate", UNSET)
        login_date: Union[Unset, datetime.datetime]
        if isinstance(_login_date, Unset):
            login_date = UNSET
        else:
            login_date = isoparse(_login_date)

        login_ip = d.pop("loginIP", UNSET)

        _last_login_date = d.pop("lastLoginDate", UNSET)
        last_login_date: Union[Unset, datetime.datetime]
        if isinstance(_last_login_date, Unset):
            last_login_date = UNSET
        else:
            last_login_date = isoparse(_last_login_date)

        last_login_ip = d.pop("lastLoginIP", UNSET)

        failed_login_attempts = d.pop("failedLoginAttempts", UNSET)

        agreed_to_terms_of_use = d.pop("agreedToTermsOfUse", UNSET)

        active = d.pop("active", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: Union[Unset, datetime.datetime]
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = isoparse(_birthday)

        comments = d.pop("comments", UNSET)

        nick_name = d.pop("nickName", UNSET)

        delete_in_progress = d.pop("deleteInProgress", UNSET)

        _delete_date = d.pop("deleteDate", UNSET)
        delete_date: Union[Unset, datetime.datetime]
        if isinstance(_delete_date, Unset):
            delete_date = UNSET
        else:
            delete_date = isoparse(_delete_date)

        password_reset = d.pop("passwordReset", UNSET)

        password_encrypted = d.pop("passwordEncrypted", UNSET)

        sms_id = d.pop("smsId", UNSET)

        aim_id = d.pop("aimId", UNSET)

        icq_id = d.pop("icqId", UNSET)

        msn_id = d.pop("msnId", UNSET)

        ym_id = d.pop("ymId", UNSET)

        favorite_activity = d.pop("favoriteActivity", UNSET)

        favorite_bible_verse = d.pop("favoriteBibleVerse", UNSET)

        favorite_food = d.pop("favoriteFood", UNSET)

        favorite_movie = d.pop("favoriteMovie", UNSET)

        favorite_music = d.pop("favoriteMusic", UNSET)

        dotted_skins = d.pop("dottedSkins", UNSET)

        rounded_skins = d.pop("roundedSkins", UNSET)

        greeting = d.pop("greeting", UNSET)

        layout_ids = d.pop("layoutIds", UNSET)

        new = d.pop("new", UNSET)

        modified = d.pop("modified", UNSET)

        user = cls(
            modification_date=modification_date,
            locale=locale,
            time_zone=time_zone,
            full_name=full_name,
            default_user=default_user,
            company_id=company_id,
            actual_company_id=actual_company_id,
            password_expired=password_expired,
            female=female,
            language_id=language_id,
            time_zone_id=time_zone_id,
            resolution=resolution,
            refresh_rate=refresh_rate,
            recipient_id=recipient_id,
            recipient_name=recipient_name,
            recipient_address=recipient_address,
            recipient_internet_address=recipient_internet_address,
            multiple_recipients=multiple_recipients,
            anonymous_user=anonymous_user,
            user_role=user_role,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            user_id=user_id,
            additional_info=additional_info,
            password_expiration_date=password_expiration_date,
            middle_name=middle_name,
            male=male,
            skin_id=skin_id,
            create_date=create_date,
            login_date=login_date,
            login_ip=login_ip,
            last_login_date=last_login_date,
            last_login_ip=last_login_ip,
            failed_login_attempts=failed_login_attempts,
            agreed_to_terms_of_use=agreed_to_terms_of_use,
            active=active,
            birthday=birthday,
            comments=comments,
            nick_name=nick_name,
            delete_in_progress=delete_in_progress,
            delete_date=delete_date,
            password_reset=password_reset,
            password_encrypted=password_encrypted,
            sms_id=sms_id,
            aim_id=aim_id,
            icq_id=icq_id,
            msn_id=msn_id,
            ym_id=ym_id,
            favorite_activity=favorite_activity,
            favorite_bible_verse=favorite_bible_verse,
            favorite_food=favorite_food,
            favorite_movie=favorite_movie,
            favorite_music=favorite_music,
            dotted_skins=dotted_skins,
            rounded_skins=rounded_skins,
            greeting=greeting,
            layout_ids=layout_ids,
            new=new,
            modified=modified,
        )

        user.additional_properties = d
        return user

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
