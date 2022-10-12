from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.fire_action_form import FireActionForm
from ...models.response_entity_view import ResponseEntityView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    action_id: str,
    *,
    client: Client,
    json_body: FireActionForm,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    index_policy: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
) -> Dict[str, Any]:
    url = "{}/v1/workflow/actions/{actionId}/fire".format(client.base_url, actionId=action_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["inode"] = inode

    params["identifier"] = identifier

    params["indexPolicy"] = index_policy

    params["language"] = language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ResponseEntityView]]:
    if response.status_code == 200:
        response_200 = ResponseEntityView.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ResponseEntityView]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    action_id: str,
    *,
    client: Client,
    json_body: FireActionForm,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    index_policy: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
) -> Response[Union[Any, ResponseEntityView]]:
    """Fire action by ID

    Args:
        action_id (str):
        inode (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        index_policy (Union[Unset, None, str]):
        language (Union[Unset, None, str]):  Default: '-1'.
        json_body (FireActionForm):

    Returns:
        Response[Union[Any, ResponseEntityView]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        client=client,
        json_body=json_body,
        inode=inode,
        identifier=identifier,
        index_policy=index_policy,
        language=language,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    action_id: str,
    *,
    client: Client,
    json_body: FireActionForm,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    index_policy: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
) -> Optional[Union[Any, ResponseEntityView]]:
    """Fire action by ID

    Args:
        action_id (str):
        inode (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        index_policy (Union[Unset, None, str]):
        language (Union[Unset, None, str]):  Default: '-1'.
        json_body (FireActionForm):

    Returns:
        Response[Union[Any, ResponseEntityView]]
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        json_body=json_body,
        inode=inode,
        identifier=identifier,
        index_policy=index_policy,
        language=language,
    ).parsed


async def asyncio_detailed(
    action_id: str,
    *,
    client: Client,
    json_body: FireActionForm,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    index_policy: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
) -> Response[Union[Any, ResponseEntityView]]:
    """Fire action by ID

    Args:
        action_id (str):
        inode (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        index_policy (Union[Unset, None, str]):
        language (Union[Unset, None, str]):  Default: '-1'.
        json_body (FireActionForm):

    Returns:
        Response[Union[Any, ResponseEntityView]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        client=client,
        json_body=json_body,
        inode=inode,
        identifier=identifier,
        index_policy=index_policy,
        language=language,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    action_id: str,
    *,
    client: Client,
    json_body: FireActionForm,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    index_policy: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
) -> Optional[Union[Any, ResponseEntityView]]:
    """Fire action by ID

    Args:
        action_id (str):
        inode (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        index_policy (Union[Unset, None, str]):
        language (Union[Unset, None, str]):  Default: '-1'.
        json_body (FireActionForm):

    Returns:
        Response[Union[Any, ResponseEntityView]]
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            json_body=json_body,
            inode=inode,
            identifier=identifier,
            index_policy=index_policy,
            language=language,
        )
    ).parsed
