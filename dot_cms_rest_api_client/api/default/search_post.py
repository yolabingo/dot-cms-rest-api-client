from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: str,
    depth: Union[Unset, None, str] = UNSET,
    live: Union[Unset, None, bool] = UNSET,
    all_categories_info: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/es/search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["depth"] = depth

    params["live"] = live

    params["allCategoriesInfo"] = all_categories_info

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: str,
    depth: Union[Unset, None, str] = UNSET,
    live: Union[Unset, None, bool] = UNSET,
    all_categories_info: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        depth (Union[Unset, None, str]):
        live (Union[Unset, None, bool]):
        all_categories_info (Union[Unset, None, bool]):
        json_body (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        depth=depth,
        live=live,
        all_categories_info=all_categories_info,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    json_body: str,
    depth: Union[Unset, None, str] = UNSET,
    live: Union[Unset, None, bool] = UNSET,
    all_categories_info: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        depth (Union[Unset, None, str]):
        live (Union[Unset, None, bool]):
        all_categories_info (Union[Unset, None, bool]):
        json_body (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        depth=depth,
        live=live,
        all_categories_info=all_categories_info,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
