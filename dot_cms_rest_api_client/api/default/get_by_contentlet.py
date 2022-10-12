from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.response_entity_permission_view import ResponseEntityPermissionView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    contentlet_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = "READ",
) -> Dict[str, Any]:
    url = "{}/v1/permissions/_bycontent".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["contentletId"] = contentlet_id

    params["type"] = type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ResponseEntityPermissionView]]:
    if response.status_code == 200:
        response_200 = ResponseEntityPermissionView.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ResponseEntityPermissionView]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    contentlet_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = "READ",
) -> Response[Union[Any, ResponseEntityPermissionView]]:
    """Get permission for a Contentlet

    Args:
        contentlet_id (Union[Unset, None, str]):
        type (Union[Unset, None, str]):  Default: 'READ'.

    Returns:
        Response[Union[Any, ResponseEntityPermissionView]]
    """

    kwargs = _get_kwargs(
        client=client,
        contentlet_id=contentlet_id,
        type=type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    contentlet_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = "READ",
) -> Optional[Union[Any, ResponseEntityPermissionView]]:
    """Get permission for a Contentlet

    Args:
        contentlet_id (Union[Unset, None, str]):
        type (Union[Unset, None, str]):  Default: 'READ'.

    Returns:
        Response[Union[Any, ResponseEntityPermissionView]]
    """

    return sync_detailed(
        client=client,
        contentlet_id=contentlet_id,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    contentlet_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = "READ",
) -> Response[Union[Any, ResponseEntityPermissionView]]:
    """Get permission for a Contentlet

    Args:
        contentlet_id (Union[Unset, None, str]):
        type (Union[Unset, None, str]):  Default: 'READ'.

    Returns:
        Response[Union[Any, ResponseEntityPermissionView]]
    """

    kwargs = _get_kwargs(
        client=client,
        contentlet_id=contentlet_id,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    contentlet_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = "READ",
) -> Optional[Union[Any, ResponseEntityPermissionView]]:
    """Get permission for a Contentlet

    Args:
        contentlet_id (Union[Unset, None, str]):
        type (Union[Unset, None, str]):  Default: 'READ'.

    Returns:
        Response[Union[Any, ResponseEntityPermissionView]]
    """

    return (
        await asyncio_detailed(
            client=client,
            contentlet_id=contentlet_id,
            type=type,
        )
    ).parsed
