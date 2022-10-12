from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.fire_merge_action_default_system_action import FireMergeActionDefaultSystemAction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    system_action: FireMergeActionDefaultSystemAction,
    *,
    client: Client,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/workflow/actions/default/fire/{systemAction}".format(client.base_url, systemAction=system_action)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["inode"] = inode

    params["identifier"] = identifier

    params["language"] = language

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    system_action: FireMergeActionDefaultSystemAction,
    *,
    client: Client,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        system_action (FireMergeActionDefaultSystemAction):
        inode (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        language (Union[Unset, None, str]):  Default: '-1'.
        offset (Union[Unset, None, int]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        system_action=system_action,
        client=client,
        inode=inode,
        identifier=identifier,
        language=language,
        offset=offset,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    system_action: FireMergeActionDefaultSystemAction,
    *,
    client: Client,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        system_action (FireMergeActionDefaultSystemAction):
        inode (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        language (Union[Unset, None, str]):  Default: '-1'.
        offset (Union[Unset, None, int]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        system_action=system_action,
        client=client,
        inode=inode,
        identifier=identifier,
        language=language,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
