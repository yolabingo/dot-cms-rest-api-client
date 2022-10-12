from typing import Any, Dict, List

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    site_name: str,
    *,
    client: Client,
    json_body: List[str],
) -> Dict[str, Any]:
    url = "{}/v1/folder/{siteName}".format(client.base_url, siteName=site_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    site_name: str,
    *,
    client: Client,
    json_body: List[str],
) -> Response[Any]:
    """
    Args:
        site_name (str):
        json_body (List[str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        site_name=site_name,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    site_name: str,
    *,
    client: Client,
    json_body: List[str],
) -> Response[Any]:
    """
    Args:
        site_name (str):
        json_body (List[str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        site_name=site_name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
