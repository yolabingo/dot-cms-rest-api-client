from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
) -> Dict[str, Any]:
    url = "{}/v1/content/resourcelinks".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["inode"] = inode

    params["identifier"] = identifier

    params["language"] = language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
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
    *,
    client: Client,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
) -> Response[Any]:
    """
    Args:
        inode (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        language (Union[Unset, None, str]):  Default: '-1'.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        inode=inode,
        identifier=identifier,
        language=language,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    inode: Union[Unset, None, str] = UNSET,
    identifier: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = "-1",
) -> Response[Any]:
    """
    Args:
        inode (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        language (Union[Unset, None, str]):  Default: '-1'.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        inode=inode,
        identifier=identifier,
        language=language,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
