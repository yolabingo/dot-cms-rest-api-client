from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    roleid: str,
    *,
    client: Client,
    role_hierarchy_for_assign: Union[Unset, None, bool] = False,
    name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/roles/{roleid}/rolehierarchyanduserroles".format(client.base_url, roleid=roleid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["roleHierarchyForAssign"] = role_hierarchy_for_assign

    params["name"] = name

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
    role_hierarchy_for_assign: Union[Unset, None, bool] = False,
    name: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        roleid (str):
        role_hierarchy_for_assign (Union[Unset, None, bool]):
        name (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        roleid=roleid,
        client=client,
        role_hierarchy_for_assign=role_hierarchy_for_assign,
        name=name,
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
    role_hierarchy_for_assign: Union[Unset, None, bool] = False,
    name: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        roleid (str):
        role_hierarchy_for_assign (Union[Unset, None, bool]):
        name (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        roleid=roleid,
        client=client,
        role_hierarchy_for_assign=role_hierarchy_for_assign,
        name=name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
