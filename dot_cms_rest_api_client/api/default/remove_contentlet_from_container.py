from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    container_id: str,
    contentlet_id: str,
    uid: str,
    *,
    client: Client,
    order: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/containers/delete/{containerId}/content/{contentletId}/uid/{uid}".format(
        client.base_url, containerId=container_id, contentletId=contentlet_id, uid=uid
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
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
    uid: str,
    *,
    client: Client,
    order: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        container_id (str):
        contentlet_id (str):
        uid (str):
        order (Union[Unset, None, int]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        contentlet_id=contentlet_id,
        uid=uid,
        client=client,
        order=order,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    container_id: str,
    contentlet_id: str,
    uid: str,
    *,
    client: Client,
    order: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        container_id (str):
        contentlet_id (str):
        uid (str):
        order (Union[Unset, None, int]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        contentlet_id=contentlet_id,
        uid=uid,
        client=client,
        order=order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
