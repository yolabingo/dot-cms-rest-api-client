from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    content_type_id: Union[Unset, None, str] = UNSET,
    show_archive: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/v1/workflow/schemes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["contentTypeId"] = content_type_id

    params["showArchive"] = show_archive

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
    content_type_id: Union[Unset, None, str] = UNSET,
    show_archive: Union[Unset, None, bool] = True,
) -> Response[Any]:
    """
    Args:
        content_type_id (Union[Unset, None, str]):
        show_archive (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        content_type_id=content_type_id,
        show_archive=show_archive,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    content_type_id: Union[Unset, None, str] = UNSET,
    show_archive: Union[Unset, None, bool] = True,
) -> Response[Any]:
    """
    Args:
        content_type_id (Union[Unset, None, str]):
        show_archive (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        content_type_id=content_type_id,
        show_archive=show_archive,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
