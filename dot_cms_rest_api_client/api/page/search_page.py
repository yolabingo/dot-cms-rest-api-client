from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    path: Union[Unset, None, str] = UNSET,
    live: Union[Unset, None, bool] = UNSET,
    only_live_sites: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/page/search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["path"] = path

    params["live"] = live

    params["onlyLiveSites"] = only_live_sites

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
    path: Union[Unset, None, str] = UNSET,
    live: Union[Unset, None, bool] = UNSET,
    only_live_sites: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        path (Union[Unset, None, str]):
        live (Union[Unset, None, bool]):
        only_live_sites (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        path=path,
        live=live,
        only_live_sites=only_live_sites,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    path: Union[Unset, None, str] = UNSET,
    live: Union[Unset, None, bool] = UNSET,
    only_live_sites: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        path (Union[Unset, None, str]):
        live (Union[Unset, None, bool]):
        only_live_sites (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        path=path,
        live=live,
        only_live_sites=only_live_sites,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
