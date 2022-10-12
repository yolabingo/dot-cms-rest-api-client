from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.response_entity_small_role_view import ResponseEntitySmallRoleView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    search_name: Union[Unset, None, str] = "",
    search_key: Union[Unset, None, str] = "",
    role_id: Union[Unset, None, str] = "",
    start: Union[Unset, None, int] = 0,
    count: Union[Unset, None, int] = 20,
    include_user_roles: Union[Unset, None, bool] = True,
    include_workflow_roles: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/v1/roles/_search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["searchName"] = search_name

    params["searchKey"] = search_key

    params["roleId"] = role_id

    params["start"] = start

    params["count"] = count

    params["includeUserRoles"] = include_user_roles

    params["includeWorkflowRoles"] = include_workflow_roles

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ResponseEntitySmallRoleView]:
    if response.status_code == 200:
        response_200 = ResponseEntitySmallRoleView.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ResponseEntitySmallRoleView]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    search_name: Union[Unset, None, str] = "",
    search_key: Union[Unset, None, str] = "",
    role_id: Union[Unset, None, str] = "",
    start: Union[Unset, None, int] = 0,
    count: Union[Unset, None, int] = 20,
    include_user_roles: Union[Unset, None, bool] = True,
    include_workflow_roles: Union[Unset, None, bool] = False,
) -> Response[ResponseEntitySmallRoleView]:
    """Search Roles

    Args:
        search_name (Union[Unset, None, str]):  Default: ''.
        search_key (Union[Unset, None, str]):  Default: ''.
        role_id (Union[Unset, None, str]):  Default: ''.
        start (Union[Unset, None, int]):
        count (Union[Unset, None, int]):  Default: 20.
        include_user_roles (Union[Unset, None, bool]):  Default: True.
        include_workflow_roles (Union[Unset, None, bool]):

    Returns:
        Response[ResponseEntitySmallRoleView]
    """

    kwargs = _get_kwargs(
        client=client,
        search_name=search_name,
        search_key=search_key,
        role_id=role_id,
        start=start,
        count=count,
        include_user_roles=include_user_roles,
        include_workflow_roles=include_workflow_roles,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    search_name: Union[Unset, None, str] = "",
    search_key: Union[Unset, None, str] = "",
    role_id: Union[Unset, None, str] = "",
    start: Union[Unset, None, int] = 0,
    count: Union[Unset, None, int] = 20,
    include_user_roles: Union[Unset, None, bool] = True,
    include_workflow_roles: Union[Unset, None, bool] = False,
) -> Optional[ResponseEntitySmallRoleView]:
    """Search Roles

    Args:
        search_name (Union[Unset, None, str]):  Default: ''.
        search_key (Union[Unset, None, str]):  Default: ''.
        role_id (Union[Unset, None, str]):  Default: ''.
        start (Union[Unset, None, int]):
        count (Union[Unset, None, int]):  Default: 20.
        include_user_roles (Union[Unset, None, bool]):  Default: True.
        include_workflow_roles (Union[Unset, None, bool]):

    Returns:
        Response[ResponseEntitySmallRoleView]
    """

    return sync_detailed(
        client=client,
        search_name=search_name,
        search_key=search_key,
        role_id=role_id,
        start=start,
        count=count,
        include_user_roles=include_user_roles,
        include_workflow_roles=include_workflow_roles,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    search_name: Union[Unset, None, str] = "",
    search_key: Union[Unset, None, str] = "",
    role_id: Union[Unset, None, str] = "",
    start: Union[Unset, None, int] = 0,
    count: Union[Unset, None, int] = 20,
    include_user_roles: Union[Unset, None, bool] = True,
    include_workflow_roles: Union[Unset, None, bool] = False,
) -> Response[ResponseEntitySmallRoleView]:
    """Search Roles

    Args:
        search_name (Union[Unset, None, str]):  Default: ''.
        search_key (Union[Unset, None, str]):  Default: ''.
        role_id (Union[Unset, None, str]):  Default: ''.
        start (Union[Unset, None, int]):
        count (Union[Unset, None, int]):  Default: 20.
        include_user_roles (Union[Unset, None, bool]):  Default: True.
        include_workflow_roles (Union[Unset, None, bool]):

    Returns:
        Response[ResponseEntitySmallRoleView]
    """

    kwargs = _get_kwargs(
        client=client,
        search_name=search_name,
        search_key=search_key,
        role_id=role_id,
        start=start,
        count=count,
        include_user_roles=include_user_roles,
        include_workflow_roles=include_workflow_roles,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    search_name: Union[Unset, None, str] = "",
    search_key: Union[Unset, None, str] = "",
    role_id: Union[Unset, None, str] = "",
    start: Union[Unset, None, int] = 0,
    count: Union[Unset, None, int] = 20,
    include_user_roles: Union[Unset, None, bool] = True,
    include_workflow_roles: Union[Unset, None, bool] = False,
) -> Optional[ResponseEntitySmallRoleView]:
    """Search Roles

    Args:
        search_name (Union[Unset, None, str]):  Default: ''.
        search_key (Union[Unset, None, str]):  Default: ''.
        role_id (Union[Unset, None, str]):  Default: ''.
        start (Union[Unset, None, int]):
        count (Union[Unset, None, int]):  Default: 20.
        include_user_roles (Union[Unset, None, bool]):  Default: True.
        include_workflow_roles (Union[Unset, None, bool]):

    Returns:
        Response[ResponseEntitySmallRoleView]
    """

    return (
        await asyncio_detailed(
            client=client,
            search_name=search_name,
            search_key=search_key,
            role_id=role_id,
            start=start,
            count=count,
            include_user_roles=include_user_roles,
            include_workflow_roles=include_workflow_roles,
        )
    ).parsed
