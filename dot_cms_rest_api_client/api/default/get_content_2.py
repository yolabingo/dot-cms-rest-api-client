from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    inode_or_identifier: str,
    *,
    client: Client,
    language: Union[Unset, None, str] = "-1",
) -> Dict[str, Any]:
    url = "{}/v1/content/{inodeOrIdentifier}".format(client.base_url, inodeOrIdentifier=inode_or_identifier)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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
    inode_or_identifier: str,
    *,
    client: Client,
    language: Union[Unset, None, str] = "-1",
) -> Response[Any]:
    """
    Args:
        inode_or_identifier (str):
        language (Union[Unset, None, str]):  Default: '-1'.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        inode_or_identifier=inode_or_identifier,
        client=client,
        language=language,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    inode_or_identifier: str,
    *,
    client: Client,
    language: Union[Unset, None, str] = "-1",
) -> Response[Any]:
    """
    Args:
        inode_or_identifier (str):
        language (Union[Unset, None, str]):  Default: '-1'.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        inode_or_identifier=inode_or_identifier,
        client=client,
        language=language,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
