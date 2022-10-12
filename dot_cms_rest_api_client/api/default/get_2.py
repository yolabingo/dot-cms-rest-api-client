from typing import Any, Dict

import httpx

from ...client import Client
from ...models.get_2_json_body import Get2JsonBody
from ...types import Response


def _get_kwargs(
    folder: str,
    *,
    client: Client,
    json_body: Get2JsonBody,
) -> Dict[str, Any]:
    url = "{}/vtl/{folder}".format(client.base_url, folder=folder)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "get",
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
    folder: str,
    *,
    client: Client,
    json_body: Get2JsonBody,
) -> Response[Any]:
    """
    Args:
        folder (str):
        json_body (Get2JsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        folder=folder,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    folder: str,
    *,
    client: Client,
    json_body: Get2JsonBody,
) -> Response[Any]:
    """
    Args:
        folder (str):
        json_body (Get2JsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        folder=folder,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
