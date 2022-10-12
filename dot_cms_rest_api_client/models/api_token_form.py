from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_token_form_claims import ApiTokenFormClaims
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTokenForm")


@attr.s(auto_attribs=True)
class ApiTokenForm:
    """
    Attributes:
        user_id (Union[Unset, str]):
        token_id (Union[Unset, str]):
        show_revoked (Union[Unset, bool]):
        expiration_seconds (Union[Unset, int]):
        network (Union[Unset, str]):
        claims (Union[Unset, ApiTokenFormClaims]):
        should_be_admin (Union[Unset, bool]):
    """

    user_id: Union[Unset, str] = UNSET
    token_id: Union[Unset, str] = UNSET
    show_revoked: Union[Unset, bool] = UNSET
    expiration_seconds: Union[Unset, int] = UNSET
    network: Union[Unset, str] = UNSET
    claims: Union[Unset, ApiTokenFormClaims] = UNSET
    should_be_admin: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        token_id = self.token_id
        show_revoked = self.show_revoked
        expiration_seconds = self.expiration_seconds
        network = self.network
        claims: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.claims, Unset):
            claims = self.claims.to_dict()

        should_be_admin = self.should_be_admin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if token_id is not UNSET:
            field_dict["tokenId"] = token_id
        if show_revoked is not UNSET:
            field_dict["showRevoked"] = show_revoked
        if expiration_seconds is not UNSET:
            field_dict["expirationSeconds"] = expiration_seconds
        if network is not UNSET:
            field_dict["network"] = network
        if claims is not UNSET:
            field_dict["claims"] = claims
        if should_be_admin is not UNSET:
            field_dict["shouldBeAdmin"] = should_be_admin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId", UNSET)

        token_id = d.pop("tokenId", UNSET)

        show_revoked = d.pop("showRevoked", UNSET)

        expiration_seconds = d.pop("expirationSeconds", UNSET)

        network = d.pop("network", UNSET)

        _claims = d.pop("claims", UNSET)
        claims: Union[Unset, ApiTokenFormClaims]
        if isinstance(_claims, Unset):
            claims = UNSET
        else:
            claims = ApiTokenFormClaims.from_dict(_claims)

        should_be_admin = d.pop("shouldBeAdmin", UNSET)

        api_token_form = cls(
            user_id=user_id,
            token_id=token_id,
            show_revoked=show_revoked,
            expiration_seconds=expiration_seconds,
            network=network,
            claims=claims,
            should_be_admin=should_be_admin,
        )

        api_token_form.additional_properties = d
        return api_token_form

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
