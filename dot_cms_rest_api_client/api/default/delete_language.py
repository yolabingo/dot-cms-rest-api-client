from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    language_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/languages/{languageId}".format(client.base_url, languageId=language_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    language_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """
    Args:
        language_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        language_id=language_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    language_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """
    Args:
        language_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        language_id=language_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
