from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
    callback: Union[Unset, None, str] = UNSET,
    force_push: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/bundlePublisher/publish".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["type"] = type

    params["callback"] = callback

    params["FORCE_PUSH"] = force_push

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
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
    type: Union[Unset, None, str] = UNSET,
    callback: Union[Unset, None, str] = UNSET,
    force_push: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        type (Union[Unset, None, str]):
        callback (Union[Unset, None, str]):
        force_push (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        type=type,
        callback=callback,
        force_push=force_push,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
    callback: Union[Unset, None, str] = UNSET,
    force_push: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        type (Union[Unset, None, str]):
        callback (Union[Unset, None, str]):
        force_push (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        type=type,
        callback=callback,
        force_push=force_push,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
