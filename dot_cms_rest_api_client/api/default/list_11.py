from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = 40,
    orderby: Union[Unset, None, str] = "mod_date",
    direction: Union[Unset, None, str] = "DESC",
    host: Union[Unset, None, str] = UNSET,
    archive: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/templates".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["filter"] = filter_

    params["page"] = page

    params["per_page"] = per_page

    params["orderby"] = orderby

    params["direction"] = direction

    params["host"] = host

    params["archive"] = archive

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
    filter_: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = 40,
    orderby: Union[Unset, None, str] = "mod_date",
    direction: Union[Unset, None, str] = "DESC",
    host: Union[Unset, None, str] = UNSET,
    archive: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        filter_ (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 40.
        orderby (Union[Unset, None, str]):  Default: 'mod_date'.
        direction (Union[Unset, None, str]):  Default: 'DESC'.
        host (Union[Unset, None, str]):
        archive (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
        page=page,
        per_page=per_page,
        orderby=orderby,
        direction=direction,
        host=host,
        archive=archive,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = 40,
    orderby: Union[Unset, None, str] = "mod_date",
    direction: Union[Unset, None, str] = "DESC",
    host: Union[Unset, None, str] = UNSET,
    archive: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        filter_ (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 40.
        orderby (Union[Unset, None, str]):  Default: 'mod_date'.
        direction (Union[Unset, None, str]):  Default: 'DESC'.
        host (Union[Unset, None, str]):
        archive (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
        page=page,
        per_page=per_page,
        orderby=orderby,
        direction=direction,
        host=host,
        archive=archive,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
