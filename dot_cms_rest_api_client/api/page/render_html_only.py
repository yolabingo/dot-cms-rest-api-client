from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uri: str,
    *,
    client: Client,
    mode: Union[Unset, None, str] = "LIVE_ADMIN",
) -> Dict[str, Any]:
    url = "{}/v1/page/renderHTML/{uri}".format(client.base_url, uri=uri)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["mode"] = mode

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
    uri: str,
    *,
    client: Client,
    mode: Union[Unset, None, str] = "LIVE_ADMIN",
) -> Response[Any]:
    """
    Args:
        uri (str):
        mode (Union[Unset, None, str]):  Default: 'LIVE_ADMIN'.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        uri=uri,
        client=client,
        mode=mode,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    uri: str,
    *,
    client: Client,
    mode: Union[Unset, None, str] = "LIVE_ADMIN",
) -> Response[Any]:
    """
    Args:
        uri (str):
        mode (Union[Unset, None, str]):  Default: 'LIVE_ADMIN'.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        uri=uri,
        client=client,
        mode=mode,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
