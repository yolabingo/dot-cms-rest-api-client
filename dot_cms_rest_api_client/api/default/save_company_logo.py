from typing import Any, Dict

import httpx

from ...client import Client
from ...models.save_company_logo_multipart_data import SaveCompanyLogoMultipartData
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: SaveCompanyLogoMultipartData,
) -> Dict[str, Any]:
    url = "{}/config/saveCompanyLogo".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
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
    multipart_data: SaveCompanyLogoMultipartData,
) -> Response[Any]:
    """
    Args:
        multipart_data (SaveCompanyLogoMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: SaveCompanyLogoMultipartData,
) -> Response[Any]:
    """
    Args:
        multipart_data (SaveCompanyLogoMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
