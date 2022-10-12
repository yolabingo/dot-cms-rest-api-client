from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    host_id: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = -1,
    direction: Union[Unset, None, str] = "ASC",
    search_param: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/themes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["hostId"] = host_id

    params["page"] = page

    params["per_page"] = per_page

    params["direction"] = direction

    params["searchParam"] = search_param

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
    host_id: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = -1,
    direction: Union[Unset, None, str] = "ASC",
    search_param: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        host_id (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: -1.
        direction (Union[Unset, None, str]):  Default: 'ASC'.
        search_param (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        host_id=host_id,
        page=page,
        per_page=per_page,
        direction=direction,
        search_param=search_param,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    host_id: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = -1,
    direction: Union[Unset, None, str] = "ASC",
    search_param: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        host_id (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: -1.
        direction (Union[Unset, None, str]):  Default: 'ASC'.
        search_param (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        host_id=host_id,
        page=page,
        per_page=per_page,
        direction=direction,
        search_param=search_param,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
