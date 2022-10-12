from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    page_id: str,
    *,
    client: Client,
    filter_: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
    orderby: Union[Unset, None, str] = "title",
    direction: Union[Unset, None, str] = "ASC",
    host_id: Union[Unset, None, str] = UNSET,
    respect_front_end_roles: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/page/{pageId}/personas".format(client.base_url, pageId=page_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["filter"] = filter_

    params["page"] = page

    params["per_page"] = per_page

    params["orderby"] = orderby

    params["direction"] = direction

    params["hostId"] = host_id

    params["respectFrontEndRoles"] = respect_front_end_roles

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
    page_id: str,
    *,
    client: Client,
    filter_: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
    orderby: Union[Unset, None, str] = "title",
    direction: Union[Unset, None, str] = "ASC",
    host_id: Union[Unset, None, str] = UNSET,
    respect_front_end_roles: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        page_id (str):
        filter_ (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):
        orderby (Union[Unset, None, str]):  Default: 'title'.
        direction (Union[Unset, None, str]):  Default: 'ASC'.
        host_id (Union[Unset, None, str]):
        respect_front_end_roles (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        page_id=page_id,
        client=client,
        filter_=filter_,
        page=page,
        per_page=per_page,
        orderby=orderby,
        direction=direction,
        host_id=host_id,
        respect_front_end_roles=respect_front_end_roles,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    page_id: str,
    *,
    client: Client,
    filter_: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
    orderby: Union[Unset, None, str] = "title",
    direction: Union[Unset, None, str] = "ASC",
    host_id: Union[Unset, None, str] = UNSET,
    respect_front_end_roles: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        page_id (str):
        filter_ (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):
        orderby (Union[Unset, None, str]):  Default: 'title'.
        direction (Union[Unset, None, str]):  Default: 'ASC'.
        host_id (Union[Unset, None, str]):
        respect_front_end_roles (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        page_id=page_id,
        client=client,
        filter_=filter_,
        page=page,
        per_page=per_page,
        orderby=orderby,
        direction=direction,
        host_id=host_id,
        respect_front_end_roles=respect_front_end_roles,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
