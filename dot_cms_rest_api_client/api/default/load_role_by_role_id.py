from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    roleid: str,
    *,
    client: Client,
    load_children_roles: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/v1/roles/{roleid}".format(client.base_url, roleid=roleid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["loadChildrenRoles"] = load_children_roles

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
    roleid: str,
    *,
    client: Client,
    load_children_roles: Union[Unset, None, bool] = True,
) -> Response[Any]:
    """
    Args:
        roleid (str):
        load_children_roles (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        roleid=roleid,
        client=client,
        load_children_roles=load_children_roles,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    roleid: str,
    *,
    client: Client,
    load_children_roles: Union[Unset, None, bool] = True,
) -> Response[Any]:
    """
    Args:
        roleid (str):
        load_children_roles (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        roleid=roleid,
        client=client,
        load_children_roles=load_children_roles,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
