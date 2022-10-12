from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    params: str,
    *,
    client: Client,
    range_: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/notification/getNotifications/{params}".format(client.base_url, params=params)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(range_, Unset):
        headers["Range"] = range_

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    params: str,
    *,
    client: Client,
    range_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        params (str):
        range_ (Union[Unset, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        params=params,
        client=client,
        range_=range_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    params: str,
    *,
    client: Client,
    range_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        params (str):
        range_ (Union[Unset, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        params=params,
        client=client,
        range_=range_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
