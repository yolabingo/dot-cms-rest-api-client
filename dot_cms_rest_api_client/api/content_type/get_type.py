from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id_or_var: str,
    *,
    client: Client,
    language_id: Union[Unset, None, int] = UNSET,
    live: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/contenttype/id/{idOrVar}".format(client.base_url, idOrVar=id_or_var)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["languageId"] = language_id

    params["live"] = live

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
    id_or_var: str,
    *,
    client: Client,
    language_id: Union[Unset, None, int] = UNSET,
    live: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        id_or_var (str):
        language_id (Union[Unset, None, int]):
        live (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id_or_var=id_or_var,
        client=client,
        language_id=language_id,
        live=live,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    id_or_var: str,
    *,
    client: Client,
    language_id: Union[Unset, None, int] = UNSET,
    live: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        id_or_var (str):
        language_id (Union[Unset, None, int]):
        live (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id_or_var=id_or_var,
        client=client,
        language_id=language_id,
        live=live,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
