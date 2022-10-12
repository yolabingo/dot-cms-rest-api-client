from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key: str,
    *,
    client: Client,
    remove_descriptor: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/apps/{key}".format(client.base_url, key=key)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["removeDescriptor"] = remove_descriptor

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
    key: str,
    *,
    client: Client,
    remove_descriptor: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        key (str):
        remove_descriptor (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        key=key,
        client=client,
        remove_descriptor=remove_descriptor,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
    remove_descriptor: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        key (str):
        remove_descriptor (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        key=key,
        client=client,
        remove_descriptor=remove_descriptor,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
