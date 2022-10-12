from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    container_id: str,
    contentlet_id: str,
    *,
    client: Client,
    page_inode: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/containers/{containerId}/content/{contentletId}".format(
        client.base_url, containerId=container_id, contentletId=contentlet_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["pageInode"] = page_inode

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
    container_id: str,
    contentlet_id: str,
    *,
    client: Client,
    page_inode: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        container_id (str):
        contentlet_id (str):
        page_inode (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        contentlet_id=contentlet_id,
        client=client,
        page_inode=page_inode,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    container_id: str,
    contentlet_id: str,
    *,
    client: Client,
    page_inode: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        container_id (str):
        contentlet_id (str):
        page_inode (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        contentlet_id=contentlet_id,
        client=client,
        page_inode=page_inode,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
