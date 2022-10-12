from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    contentlet_id: str,
    *,
    client: Client,
    container_id: Union[Unset, None, str] = UNSET,
    page_inode: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/containers/content/{contentletId}".format(client.base_url, contentletId=contentlet_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["containerId"] = container_id

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
    contentlet_id: str,
    *,
    client: Client,
    container_id: Union[Unset, None, str] = UNSET,
    page_inode: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        contentlet_id (str):
        container_id (Union[Unset, None, str]):
        page_inode (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        contentlet_id=contentlet_id,
        client=client,
        container_id=container_id,
        page_inode=page_inode,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    contentlet_id: str,
    *,
    client: Client,
    container_id: Union[Unset, None, str] = UNSET,
    page_inode: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        contentlet_id (str):
        container_id (Union[Unset, None, str]):
        page_inode (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        contentlet_id=contentlet_id,
        client=client,
        container_id=container_id,
        page_inode=page_inode,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
